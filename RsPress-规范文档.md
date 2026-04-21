# RsPress 知识库生成规范

## 1. 技术栈概览

### 核心技术

- **RsPress**：基于 React + MDX + Rsbuild + Rspack（Rust）的静态站点生成器
- **SQLite**：轻量级数据库，用于存储元数据和索引
- **React 19**：前端框架
- **TypeScript**：类型安全的 JavaScript 超集
- **Git**：版本控制系统

## 2. RsPress 项目结构

```
├── .agent/            # AI 辅助开发上下文文件夹
│   ├── context.md     # 项目上下文和背景信息
│   ├── skills/        # 自定义技能定义
│   │   ├── agent-dev.md
│   │   └── doc-write.md
│   ├── constraints/   # AI 需遵守的约束规范
│   │   ├── code-style.md
│   │   └── security.md
│   └── workflows/     # 工作流程定义
│       └── add-doc.md
├── .rsbuild/          # Rsbuild 配置目录
├── .rspress/          # RsPress 配置目录
├── docs/              # 文档源码目录
│   ├── 01-基础理论/    # 对应知识库结构
│   ├── 02-技术栈详解/  
│   ├── 03-Harness工程/
│   ├── 04-框架工具/
│   ├── 05-应用场景/
│   ├── 06-实践项目/
│   ├── 07-资源汇总/
│   ├── index.md       # 首页
│   └── _meta.json     # 导航配置
├── src/               # 自定义组件和工具
│   ├── components/    # React 组件
│   ├── hooks/         # 自定义 Hooks
│   └── utils/         # 工具函数
├── public/            # 静态资源
├── package.json       # 项目配置
├── tsconfig.json      # TypeScript 配置
└── README.md          # 项目说明
```

## 3. .agent 文件夹规范

### 3.1 文件夹用途

`.agent` 文件夹用于存放 AI 辅助开发时需要的上下文信息，包括项目背景、开发规范、自定义技能等，确保 AI 能够更好地理解和参与项目开发。

### 3.2 子文件夹结构

```
.agent/
├── context.md         # 项目上下文
├── skills/            # 自定义技能
├── constraints/       # 约束规范
└── workflows/         # 工作流程
```

### 3.3 context.md - 项目上下文

```markdown
# 项目上下文

## 项目概述
- 项目名称：AI Agent 实践学习知识库
- 项目描述：一个专注于 AI Agent 实践和应用的学习知识库
- 技术栈：RsPress + SQLite + React 19 + TypeScript + Git

## 目标用户
- 对 AI Agent 感兴趣的开发者
- 希望学习 AI Agent 开发的初学者
- 有经验的开发者想要系统学习 Agent 技术

## 核心功能
1. 文档展示：结构化展示 AI Agent 学习内容
2. 搜索功能：基于 SQLite FTS5 的全文搜索
3. 导航系统：清晰的多级导航
4. 自定义组件：增强的展示组件
5. 数据同步：文档与数据库的自动同步

## 开发理念
- 简洁：保持代码和文档的简洁性
- 可维护：遵循最佳实践，易于维护
- 可扩展：设计具有扩展性的架构
- 用户友好：提供良好的用户体验

## 重要文件
- `学习路径大纲.md`：详细的学习路径规划
- `AGENT.md`：知识库定位和核心主题
```

### 3.4 skills/ - 自定义技能

#### skills/agent-dev.md
```markdown
# Agent 开发技能

## 目标
帮助开发者快速实现 AI Agent 相关功能。

## 能力
1. 快速实现基础 Agent 结构
2. 推荐合适的工具和库
3. 提供代码示例和最佳实践
4. 帮助调试 Agent 相关问题

## 工作流程
1. 理解需求
2. 推荐技术方案
3. 提供代码示例
4. 帮助测试和优化
```

#### skills/doc-write.md
```markdown
# 文档写作技能

## 目标
帮助编写符合规范的知识库文档。

## 能力
1. 遵循 RsPress 文档规范
2. 使用正确的 Markdown 格式
3. 提供代码示例
4. 确保文档结构清晰

## 文档结构要求
```markdown
---
title: 文档标题
description: 文档描述
author: 作者
date: YYYY-MM-DD
category: 分类
---

# 主要内容
...
```
```

### 3.5 constraints/ - 约束规范

#### constraints/code-style.md
```markdown
# 代码风格规范

## TypeScript/React
1. 使用函数组件而非类组件
2. 使用 TypeScript 类型注解
3. 使用 ES6+ 语法
4. 遵循 Airbnb JavaScript Style Guide
5. 使用 2 空格缩进

## 组件命名
1. 使用 PascalCase 命名组件
2. 文件名与组件名一致
3. 使用描述性的组件名

## 代码组织
1. 单一职责原则
2. 组件和样式分离
3. 合理使用 TypeScript 接口
4. 避免代码重复
```

#### constraints/security.md
```markdown
# 安全规范

## 一般原则
1. 不要在代码中提交敏感信息
2. 使用环境变量存储配置
3. 输入验证和清理
4. 遵循安全最佳实践

## 文档安全
1. 避免在文档中包含敏感信息
2. 检查示例代码中的硬编码值
3. 确保链接安全
```

### 3.6 workflows/ - 工作流程

#### workflows/add-doc.md
```markdown
# 添加新文档工作流

## 步骤
1. 确定文档在知识库中的位置
2. 创建新的 Markdown/MDX 文件
3. 添加必要的 frontmatter
4. 编写文档内容
5. 更新 _meta.json 导航配置
6. 测试文档渲染
7. 提交代码

## 检查清单
- [ ] 文档路径正确
- [ ] frontmatter 完整
- [ ] 内容结构清晰
- [ ] 代码示例正确
- [ ] 导航已更新
- [ ] 渲染无错误
```

## 4. 配置文件规范

### 4.1 package.json

```json
{
  "name": "ai-agent-knowledge-base",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "rspress dev",
    "build": "rspress build",
    "preview": "rspress preview",
    "lint": "eslint . --ext .ts,.tsx,.md,.mdx",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  },
  "devDependencies": {
    "@rspress/core": "^1.0.0",
    "@rspress/plugin-shiki": "^1.0.0",
    "@rspress/plugin-medium-zoom": "^1.0.0",
    "typescript": "^5.0.0",
    "eslint": "^8.0.0",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0"
  }
}
```

### 4.2 .rspress/config.ts

```typescript
import { defineConfig } from '@rspress/core';

export default defineConfig({
  title: 'AI Agent 实践学习知识库',
  description: '系统学习 AI Agent 开发、设计和应用',
  base: '/',
  lang: 'zh-CN',
  theme: {
    darkMode: true,
    pagination: true,
    logo: {
      light: '/logo-light.svg',
      dark: '/logo-dark.svg'
    },
    nav: [
      {
        text: '首页',
        link: '/'
      },
      {
        text: '基础理论',
        link: '/01-基础理论/'
      },
      {
        text: '技术栈详解',
        link: '/02-技术栈详解/'
      },
      {
        text: 'Harness 工程',
        link: '/03-Harness工程/'
      },
      {
        text: '框架工具',
        link: '/04-框架工具/'
      },
      {
        text: '应用场景',
        link: '/05-应用场景/'
      },
      {
        text: '实践项目',
        link: '/06-实践项目/'
      },
      {
        text: '资源汇总',
        link: '/07-资源汇总/'
      }
    ]
  },
  plugins: [
    '@rspress/plugin-shiki',
    '@rspress/plugin-medium-zoom'
  ],
  markdown: {
    mdxRs: true,
    syntaxHighlighter: 'shiki',
    shiki: {
      theme: 'github-dark'
    }
  },
  builderConfig: {
    output: {
      assetPrefix: '/'
    }
  }
});
```

### 4.3 docs/_meta.json

```json
{
  "01-基础理论": {
    "title": "基础理论",
    "order": 1
  },
  "02-技术栈详解": {
    "title": "技术栈详解",
    "order": 2,
    "children": {
      "提示词工程": {
        "title": "提示词工程",
        "order": 1
      },
      "上下文工程": {
        "title": "上下文工程",
        "order": 2
      }
    }
  },
  "03-Harness工程": {
    "title": "Harness 工程",
    "order": 3,
    "children": {
      "管道编排": {
        "title": "管道编排",
        "order": 1
      },
      "状态管理": {
        "title": "状态管理",
        "order": 2
      },
      "可观测性": {
        "title": "可观测性",
        "order": 3
      },
      "测试评估": {
        "title": "测试评估",
        "order": 4
      }
    }
  },
  "04-框架工具": {
    "title": "框架工具",
    "order": 4
  },
  "05-应用场景": {
    "title": "应用场景",
    "order": 5
  },
  "06-实践项目": {
    "title": "实践项目",
    "order": 6
  },
  "07-资源汇总": {
    "title": "资源汇总",
    "order": 7
  }
}
```

## 5. 文档编写规范

### 5.1 Markdown/MDX 规范

#### 基本结构

````mdx
---
title: 文档标题
description: 文档描述
author: 作者
date: 2026-04-21
category: 分类
---

# 主标题

## 副标题

### 三级标题

#### 四级标题

## 5.2 代码块

```typescript
// 代码示例
function example() {
  return 'Hello RsPress';
}
```
````

## 5.3 组件使用

```mdx
import { Alert, CodeBlock } from '@components';

<Alert type="info">
  这是一个信息提示
</Alert>

<CodeBlock language="typescript">
{`
// 代码示例
const x = 10;
`}
</CodeBlock>
```

## 5.4 表格

| 列1  | 列2  | 列3  |
| --- | --- | --- |
| 内容1 | 内容2 | 内容3 |
| 内容4 | 内容5 | 内容6 |

## 5.5 链接

- [内部链接](/01-基础理论/)
- [外部链接](https://example.com)

## 5.6 图片

![图片描述](/images/example.png)

## 6. 组件开发规范

### 6.1 组件目录结构

```
src/components/
├── Alert/
│   ├── index.tsx
│   └── styles.module.css
├── CodeBlock/
│   ├── index.tsx
│   └── styles.module.css
└── index.ts  # 导出所有组件
```

### 6.2 组件示例

```typescript
// src/components/Alert/index.tsx
import React from 'react';
import styles from './styles.module.css';

type AlertType = 'info' | 'success' | 'warning' | 'error';

interface AlertProps {
  type?: AlertType;
  children: React.ReactNode;
}

export function Alert({ type = 'info', children }: AlertProps) {
  return (
    <div className={`${styles.alert} ${styles[`alert-${type}`]}`}>
      {children}
    </div>
  );
}
```

## 7. 最佳实践

### 7.1 性能优化

1. **代码分割**：使用动态导入减少初始加载时间
2. **图片优化**：使用适当的图片格式和大小
3. **缓存策略**：合理设置缓存头
4. **预加载**：对关键资源使用预加载

### 7.2 SEO 优化

1. **元数据**：为每个页面设置合适的 title 和 description
2. **结构化数据**：使用 JSON-LD 格式的结构化数据
3. **面包屑导航**：实现清晰的面包屑导航
4. **站点地图**：生成站点地图

### 7.3 可访问性

1. **语义化 HTML**：使用适当的 HTML 标签
2. **键盘导航**：确保所有功能可通过键盘访问
3. **屏幕阅读器**：支持屏幕阅读器
4. **颜色对比度**：确保文本和背景的对比度符合标准

### 7.4 国际化

1. **多语言支持**：使用 RsPress 的国际化功能
2. **翻译管理**：集中管理翻译资源
3. **日期和时间**：根据用户地区显示

## 8. SQLite 集成方案

### 8.1 数据库结构

```sql
-- 文档表
CREATE TABLE IF NOT EXISTS documents (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  path TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  author TEXT,
  date TEXT,
  category TEXT,
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 标签表
CREATE TABLE IF NOT EXISTS tags (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

-- 文档-标签关联表
CREATE TABLE IF NOT EXISTS document_tags (
  document_id INTEGER,
  tag_id INTEGER,
  PRIMARY KEY (document_id, tag_id),
  FOREIGN KEY (document_id) REFERENCES documents(id),
  FOREIGN KEY (tag_id) REFERENCES tags(id)
);

-- 搜索索引表
CREATE VIRTUAL TABLE IF NOT EXISTS search_index USING fts5(
  title,
  content,
  path,
  tokenize='porter'
);
```

### 8.2 数据同步

1. **构建时同步**：在 RsPress 构建过程中同步文档到 SQLite
2. **增量更新**：只同步修改的文档
3. **搜索索引**：自动更新搜索索引

## 9. 部署方案

### 9.1 构建流程

1. **安装依赖**：`npm install`
2. **类型检查**：`npm run typecheck`
3. **代码检查**：`npm run lint`
4. **构建站点**：`npm run build`
5. **同步数据库**：执行数据同步脚本

### 9.2 部署平台

- **GitHub Pages**：适合静态站点
- **Vercel**：支持自动部署
- **Netlify**：简单易用
- **自建服务器**：完全控制

### 9.3 CI/CD 配置

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      - run: npm install
      - run: npm run typecheck
      - run: npm run lint
      - run: npm run build
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

## 10. 开发工作流

### 10.1 本地开发

1. **启动开发服务器**：`npm run dev`
2. **访问本地站点**：`http://localhost:3000`
3. **实时预览**：修改文件后自动刷新

### 10.2 分支管理

- **main**：主分支，部署生产环境
- **dev**：开发分支，集成测试
- **feature/**：功能分支，开发新功能
- **fix/**：修复分支，修复 bug

### 10.3 代码提交规范

使用 Conventional Commits 规范：

- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档修改
- `style`: 代码风格
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建或依赖更新

## 11. 监控与维护

### 11.1 监控

- **访问统计**：使用 Google Analytics 或 Matomo
- **性能监控**：使用 Lighthouse 或 WebPageTest
- **错误监控**：使用 Sentry

### 11.2 维护

- **定期更新**：更新依赖包
- **备份**：定期备份数据库和代码
- **安全检查**：定期检查安全漏洞
- **内容更新**：定期更新文档内容

## 12. 总结

本规范文档提供了使用 RsPress 构建 AI Agent 知识库的完整指南，包括项目结构、配置、文档编写规范、最佳实践等。遵循本规范可以确保知识库的质量和可维护性，为学习者提供更好的学习体验。

随着技术的发展和需求的变化，本规范将不断更新和完善。
