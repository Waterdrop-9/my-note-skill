#!/usr/bin/env python3
"""Run the code readers actually see in the cache example (standard library only)."""
from html.parser import HTMLParser
from pathlib import Path


class CodeBlock(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "code" and dict(attrs).get("id") == "cache-code":
            self.active = True

    def handle_endtag(self, tag):
        if tag == "code":
            self.active = False

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)


def main():
    path = Path(__file__).resolve().parents[1] / "examples/deep-study-cache.html"
    block = CodeBlock()
    block.feed(path.read_text())
    assert block.parts, "Example code block missing"
    namespace = {}
    exec(compile("".join(block.parts), str(path), "exec"), namespace)
    cache_type = namespace["LRUCache"]
    calls = []

    def load(key):
        calls.append(key)
        return key.lower()

    cache = cache_type(2)
    expected = [["A"], ["A", "B"], ["B", "A"], ["A", "C"], ["C", "B"]]
    for key, order in zip("ABACB", expected):
        assert cache.get(key, load) == key.lower()
        assert list(cache.items) == order
        assert len(cache.items) <= cache.capacity
    assert calls == list("ABCB"), "A hit must not call load"

    def fail(key):
        raise RuntimeError("load failed")

    before = list(cache.items.items())
    try:
        cache.get("D", fail)
    except RuntimeError:
        pass
    else:
        raise AssertionError("Load exception must propagate")
    assert list(cache.items.items()) == before, "Failure must preserve cached values"

    empty = cache_type(0)
    empty.get("A", load)
    empty.get("A", load)
    assert not empty.items and calls[-2:] == ["A", "A"]
    nullable = cache_type(1)
    assert nullable.get("A", lambda key: None) is None
    assert nullable.get("A", fail) is None, "None is a valid cached value"

    scan = cache_type(2)
    calls.clear()
    for key in "ABCABC":
        scan.get(key, load)
    assert calls == list("ABCABC"), "Cyclic scan should miss on every request"
    for invalid in [-1, 1.5, True]:
        try:
            cache_type(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Invalid capacity accepted: {invalid!r}")
    assert abs((1 + (1 - 0.8) * 9) - 2.8) < 1e-12
    assert 1 + (1 - 0) * 9 == 10
    print("PASS: HTML example code, access trace, failure, zero capacity, None, scan and arithmetic")


if __name__ == "__main__":
    main()
