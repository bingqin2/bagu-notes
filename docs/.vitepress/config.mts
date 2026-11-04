import { defineConfig } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import { fileURLToPath } from 'node:url'
import { buildSidebar } from './sidebar'

const docsDir = fileURLToPath(new URL('..', import.meta.url))

export default withMermaid(
  defineConfig({
    lang: 'zh-CN',
    title: '八股知识库',
    description: '按模块整理 Java 后端八股，按公司索引近两年真题',
    base: process.env.BASE ?? '/',
    lastUpdated: true,
    cleanUrls: true,
    themeConfig: {
      nav: [
        { text: '首页', link: '/' },
        { text: '近两年考什么', link: '/trends' },
        { text: '按公司', link: '/companies/' },
      ],
      sidebar: buildSidebar(docsDir),
      outline: { level: [2, 3], label: '本页目录' },
      search: { provider: 'local' },
      docFooter: { prev: '上一篇', next: '下一篇' },
    },
    mermaid: {},
  }),
)
