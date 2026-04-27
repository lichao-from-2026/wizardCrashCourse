/**
 * 状态选择器相关常量
 * 描述：定义状态选择器显示文本、图标和颜色等配置
 * 作者：AI Assistant
 * 日期：2026-04-27
 */
import type { StatusType } from '../types/doc-status';

/**
 * 状态配置
 * 描述：定义不同状态的显示文本、图标、颜色和背景色
 */
export const statusConfig: Record<StatusType, {
  label: string; // 状态显示文本
  icon: string; // 状态图标
  color: string; // 状态颜色
  bgColor: string; // 背景颜色
}> = {
  /**
   * 待完成状态
   */
  pending: {
    label: '待完成',
    icon: '○',
    color: '#94a3b8',
    bgColor: '#f1f5f9',
  },
  /**
   * 进行中状态
   */
  'in-progress': {
    label: '进行中',
    icon: '◐',
    color: '#f59e0b',
    bgColor: '#fef3c7',
  },
  /**
   * 已完成状态
   */
  completed: {
    label: '已完成',
    icon: '●',
    color: '#10b981',
    bgColor: '#d1fae5',
  },
};
