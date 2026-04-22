# AI Agent 实践学习知识库

一个专注于 AI Agent 开发、设计和应用的学习知识库。

## 技术栈

- **RsPress**：基于 React + MDX + Rsbuild + Rspack 的静态站点生成器
- **React 19**：前端框架
- **TypeScript**：类型安全
- **SQLite**：轻量级数据库
- **Git**：版本控制

## 快速开始

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产版本
npm run preview
```

## 项目结构

不要更新 docs 文件夹下的结构。

```
.
├── .rsbuild/                # Rsbuild 配置目录
├── .rspress/                # RsPress 配置目录
├── .trae/                   # Trae Solo AI 辅助开发上下文
│   ├── context.md           # 项目上下文
│   ├── AGENT.md             # 项目规范和指引（必读）
│   ├── skills/              # 自定义技能
│   │   ├── agent-dev.md
│   │   └── doc-write.md
│   ├── constraints/         # 约束规范
│   │   ├── 文档和内容格式规范.md
│   │   ├── Trae Solo行为约束.md
│   │   ├── RsPress构建规则.md
│   │   ├── code-style.md
│   │   └── security.md
│   └── workflows/           # 工作流程
│       └── add-doc.md
├── docs/                    # 文档目录
│   ├── 00-前置知识/         # 前置知识
│   │   ├── 01-AI基础概念/
│   │   ├── 02-LLM基础/
│   │   ├── 03-核心技术/
│   │   ├── 04-Agent概念/
│   │   └── 05-框架协议/
│   ├── ...
│   ├── index.md             # 首页
│   └── _meta.json           # 导航配置
├── src/                     # 自定义组件和工具
│   ├── components/          # React 组件
│   ├── hooks/               # 自定义 Hooks
│   └── utils/               # 工具函数
├── public/                  # 静态资源
├── rspress.config.ts        # RsPress 配置
├── tsconfig.json            # TypeScript 配置
├── package.json             # 项目依赖
├── README.md                # 项目说明
├── 核心主题.md              # 核心主题
├── 学习路径大纲.md          # 学习路径
└── 配置说明.md              # 配置文件说明（含中文注释）
```

## 文档规范

详细的文档规范请参考：

- [.trae/AGENT.md](./.trae/AGENT.md)：知识库规范和约束（必读）
- [.trae/constraints/文档和内容格式规范.md](./.trae/constraints/文档和内容格式规范.md)：文档格式和内容要求
- \[.trae/constraints/Trae Solo行为约束.md]\(./.trae/constraints/Trae Solo行为约束.md)：AI 辅助开发的行为规范
- [.trae/constraints/RsPress构建规则.md](./.trae/constraints/RsPress构建规则.md)：项目结构和构建规则
- [配置说明.md](./配置说明.md)：项目配置文件的详细说明（含中文注释）
- [核心主题.md](./核心主题.md)：核心主题结构和学习路径参考
- [学习路径大纲.md](./学习路径大纲.md)：详细的学习路径规划

## 开发指南

### 创建新文档

1. 在 `docs/` 对应目录下创建 Markdown 文件
2. 添加 Frontmatter 元数据
3. 遵循文档结构要求
4. 确保格式符合规范

### 使用自定义组件

如需使用自定义组件，将文件扩展名改为 `.mdx`，然后导入并使用组件。

## 许可证

MIT
