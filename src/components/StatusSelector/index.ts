/**
 * 状态选择器导出文件
 * 描述：集中导出 StatusSelector 组件及其相关类型和 Hook
 * 作者：AI Assistant
 * 日期：2026-04-27
 */

// 导出组件本身和默认导出
export { StatusSelector, default } from './StatusSelector';

// 导出类型定义（从全局类型导入再导出）
export type { StatusItem, StatusSelectorProps, StatusType } from '../../types/doc-status';

// 导出组件专用 Hook
export { useStatusSelector } from './hooks';
