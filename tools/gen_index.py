"""根据每个条目的 frontmatter（title / freq / status / summary）重新生成各模块的 index.md。

新增条目：在模块文件夹里复制一个条目文件改内容，然后运行
    python3 tools/gen_index.py
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
SKIP = {"public", "companies"}


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            v = v.strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1].replace('\\"', '"')
            out[k.strip()] = v
    return out


def module_name(d):
    idx = d / "index.md"
    if idx.exists():
        h = re.search(r"^#\s+(.+)$", idx.read_text(), re.M)
        if h:
            return h.group(1).strip()
    return d.name


def mm(s):
    # Mermaid mindmap 结点文字里不能有括号等符号
    s = re.sub(r"[（(].*?[)）]", "", s)
    return re.sub(r"[\"'`:：、，,/]", " ", s).strip()


for d in sorted(p for p in DOCS.iterdir() if p.is_dir() and not p.name.startswith(".") and p.name not in SKIP):
    name = module_name(d)
    items = []
    for f in sorted(d.glob("*.md")):
        if f.name == "index.md":
            continue
        fm = frontmatter(f.read_text())
        items.append((int(fm.get("freq", 1)), f.stem, fm))
    items.sort(key=lambda x: -x[0])
    done = sum(1 for _, _, fm in items if fm.get("status") == "done")
    tree = "\n".join(f"    {mm(fm.get('title', s))}" for _, s, fm in items)
    rows = "\n".join(
        f"| [{fm.get('title', s)}](./{s}) | {'★' * fr}{'☆' * (3 - fr)} | {'✅' if fm.get('status') == 'done' else '·'} | {fm.get('summary', '')} |"
        for fr, s, fm in items
    )
    (d / "index.md").write_text(f"""# {name}

> 进度：{done} / {len(items)} 条已写完。本页由 `tools/gen_index.py` 生成，改条目后重新运行即可。

## 知识地图

```mermaid
mindmap
  root(({mm(name)}))
{tree}
```

## 条目（按频率排序）

频率按 2025–2026 年后端面经里出现的次数估计：★★★ 几乎每场都可能问，★★ 经常问，★ 偶尔问。

| 知识点 | 频率 | 状态 | 一句话答案 |
|---|---|---|---|
{rows}
""")
    print(f"{d.name}: {len(items)} 条，{done} 条已完成")
