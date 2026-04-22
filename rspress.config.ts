// 导入 RsPress 配置函数
import { defineConfig } from 'rspress/config';
// 导入 SSG-MD 插件
import { pluginLlms } from '@rspress/plugin-llms';

// 导出 RsPress 配置
export default defineConfig({
    // 网站标题 - 在浏览器标签页中显示
    title: 'AI Agent 实践学习知识库',
    // 网站描述 - 用于搜索引擎和元数据
    description: '系统学习 AI Agent 开发、设计和应用',
    // 文档根目录 - 存放所有文档的目录
    root: 'docs',
    // 基础路径 - 网站部署的基础 URL
    base: '/',
    // 图标配置
    icon: 'https://avatars.githubusercontent.com/u/51900016?v=4',
    // 主题配置
    themeConfig: {
        // 启用暗色模式 - 允许用户切换暗色/亮色主题
        darkMode: true,
        // 社交链接
        socialLinks: [
            { icon: 'github', mode: 'link', content: 'https://github.com' }
        ],
        // 底部 footer
        footer: {
            message: '使用 RsPress 构建'
        }
    },
    // 开启 SSG (静态站点生成) - 配置为 true 或使用对象配置 { strict?: boolean }
    ssg: true,
    // 插件配置
    plugins: [
        // SSG-MD 插件 - 为 LLM 生成 Markdown 文件，包括 llms.txt 和 llms-full.txt
        pluginLlms() as any
    ]
});
