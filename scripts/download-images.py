#!/usr/bin/env python3
"""
图片下载脚本
用于下载图片到 public/images/{章节}/ 目录
"""

import os
import re
import argparse
import requests
from urllib.parse import urlparse
from pathlib import Path

# 配置
PROJECT_ROOT = Path(__file__).parent.parent
PUBLIC_DIR = PROJECT_ROOT / "public"
IMAGES_DIR = PUBLIC_DIR / "images"

# 确保目录存在
IMAGES_DIR.mkdir(parents=True, exist_ok=True)


def sanitize_filename(filename):
    """清理文件名，移除非法字符"""
    # 移除或替换非法字符
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filename = re.sub(r'\s+', '-', filename.strip())
    return filename


def get_file_extension(url):
    """从 URL 获取文件扩展名"""
    parsed = urlparse(url)
    path = parsed.path.lower()
    
    # 尝试从路径获取扩展名
    if path.endswith('.png'):
        return '.png'
    elif path.endswith('.jpg') or path.endswith('.jpeg'):
        return '.jpg'
    elif path.endswith('.gif'):
        return '.gif'
    elif path.endswith('.svg'):
        return '.svg'
    elif path.endswith('.webp'):
        return '.webp'
    
    # 默认返回 png
    return '.png'


def download_image(url, save_path, timeout=10):
    """
    下载图片到指定路径
    返回 (成功: bool, 消息: str)
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        # 检查是否是图片内容
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            return False, f"URL 返回的不是图片: {content_type}"
        
        # 保存图片
        with open(save_path, 'wb') as f:
            f.write(response.content)
        
        return True, f"下载成功: {save_path}"
    
    except requests.exceptions.RequestException as e:
        return False, f"下载失败: {str(e)}"


def main():
    parser = argparse.ArgumentParser(description='下载图片到本地知识库')
    parser.add_argument('url', help='图片 URL')
    parser.add_argument('--chapter', '-c', required=True, help='章节名称，如 "00-前置知识"')
    parser.add_argument('--name', '-n', required=True, help='描述性文件名，如 "agent-architecture-overview"')
    
    args = parser.parse_args()
    
    # 创建章节目录
    chapter_dir = IMAGES_DIR / args.chapter
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    # 获取文件扩展名
    ext = get_file_extension(args.url)
    
    # 清理文件名
    clean_name = sanitize_filename(args.name)
    filename = f"{clean_name}{ext}"
    save_path = chapter_dir / filename
    
    print(f"正在下载图片...")
    print(f"URL: {args.url}")
    print(f"保存到: {save_path}")
    
    # 下载图片
    success, message = download_image(args.url, save_path)
    
    print(f"\n结果: {message}")
    
    if success:
        # 显示 Markdown 引用路径
        relative_path = f"/images/{args.chapter}/{filename}"
        print(f"\nMarkdown 引用: ![{args.name}]({relative_path})")
    else:
        # 显示下载失败提示
        print(f"\n:::warning")
        print(f"[图片来源]({args.url}) - 下载失败，请手动下载")
        print(f":::")


if __name__ == "__main__":
    main()
