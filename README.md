# bagu-notes：八股知识库

网页版：https://bingqin2.github.io/bagu-notes/

按模块整理的 Java 后端八股，加上按公司索引的 2025–2026 年真题。网站用 VitePress 搭建，Markdown 和 Mermaid 图在 GitHub 上也能直接看。

## 本地运行

```bash
npm install
npm run dev
```

## 结构

- `docs/trends.md`：近两年考点统计
- `docs/01-java-basic/` … `docs/13-ai-agent/`：每个模块一个文件夹，每个知识点一页
- `docs/companies/`：字节、腾讯、美团、阿里的真题列表，每题链接到对应条目
- `tools/gen_index.py`：根据条目的 frontmatter 重新生成各模块总览页

## 条目格式

每个条目的 frontmatter 有 `title`、`freq`（1–3）、`status`（todo / done）、`summary`（一句话答案），正文分五段：一句话答案、展开、图解、追问链、我的项目里。写完一条把 `status` 改成 `done`，再运行：

```bash
python3 tools/gen_index.py
```
