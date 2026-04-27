/**
 * 文档状态表格导出文件
 * 描述：集中导出 DocStatusTable 组件及其相关类型和 Hook
 * 作者：AI Assistant
 * 日期：2026-04-27
 */

// 导出组件本身和默认导出
export { DocStatusTable, default } from './DocStatusTable';

// 导出类型定义（从全局类型导入再导出）
export type { DocStatusItem, DocStatusTableProps, DocStatus } from '../../types/doc-status';

// 导出组件专用 Hook
export { useDocStatusTable } from './hooks';
