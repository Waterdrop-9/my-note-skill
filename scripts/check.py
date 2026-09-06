#!/usr/bin/env python3
"""Check maintained skill resources without modifying them or requiring packages.

A focused structural check, not a full HTML/CSS validator or a content-quality score.
User-provided exemplars outside assets/examples/references are intentionally excluded.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
VOID = set("area base br col embed hr img input link meta param source track wbr".split())


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.links, self.scripts, self.errors = [], [], [], []
        self.ids = set()
        self.script = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.errors.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "script" and not attrs.get("src"):
            self.script = []
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"unexpected closing tag: {tag}")
        else:
            self.stack.pop()
        if tag == "script" and self.script is not None:
            self.scripts.append("".join(self.script))
            self.script = None

    def handle_data(self, data):
        if self.script is not None:
            self.script.append(data)


def markdown_text(text, errors):
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r"\s*(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, suffix = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    if fence is not None:
        errors.append("unclosed Markdown code fence")
    return re.sub(r"`[^`\n]*`", "", "\n".join(lines))


def main():
    paths = [ROOT / "SKILL.md", ROOT / "README.md"]
    paths += sorted((ROOT / "references").glob("*.md"))
    paths += sorted((ROOT / "assets").glob("*.html"))
    paths += sorted((ROOT / "examples").glob("*.html"))
    documents, references, issues = {}, {}, []
    node = shutil.which("node")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        errors = []
        if path.suffix == ".html":
            doc = Document()
            doc.feed(text)
            doc.close()
            documents[path] = doc
            errors.extend(doc.errors)
            if doc.stack:
                errors.append(f"unclosed tags: {doc.stack}")
            references[path] = doc.links
            if node:
                for index, script in enumerate(doc.scripts):
                    result = subprocess.run([node, "--check"], input=script, text=True, capture_output=True)
                    if result.returncode:
                        errors.append(f"inline script {index}: {result.stderr.strip()}")
        else:
            prose = markdown_text(text, errors)
            references[path] = re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", prose)
        issues.extend(f"{path.relative_to(ROOT)}: {error}" for error in errors)

    for path, links in references.items():
        for link in links:
            url = urlsplit(link.strip("<>"))
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.exists():
                issues.append(f"{path.relative_to(ROOT)}: missing local target {link}")
            elif url.fragment and target in documents and unquote(url.fragment) not in documents[target].ids:
                issues.append(f"{path.relative_to(ROOT)}: missing HTML anchor {link}")
    if issues:
        raise SystemExit("\n".join(issues))
    print(f"PASS: {len(paths)} files, local links, HTML tags/anchors, Markdown fences")
    print("PASS: inline JavaScript syntax" if node else "SKIP: Node unavailable; inline JavaScript syntax not checked")


if __name__ == "__main__":
    main()
