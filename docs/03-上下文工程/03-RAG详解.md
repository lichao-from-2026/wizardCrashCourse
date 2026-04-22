---
title: RAG详解
description: 检索增强生成（RAG）技术详解，原理、流程、实现
author: AI Agent 知识库团队
date: 2026-04-22
category: 上下文工程
---

# 一、RAG详解

RAG（Retrieval-Augmented Generation，检索增强生成）是将检索和生成结合的技术。

## 1. 什么是 RAG

### 1.1 基本概念

| 部分 | 说明 |
|------|------|
| **R (Retrieval)** | 从知识库中检索相关信息 |
| **A (Augmented)** | 用检索到的信息增强上下文 |
| **G (Generation)** | 基于增强后的上下文生成回答 |

### 1.2 为什么需要 RAG

**问题：**
- LLM 知识有时效性限制
- LLM 不知道私有数据
- 可能产生幻觉（编造内容）

**解决方案：RAG**
- 提供实时、准确的外部知识
- 可以使用私有数据
- 减少幻觉，提高可信度

## 2. RAG工作流程

### 2.1 完整流程

```
1. 准备阶段
   ├─ 收集文档
   ├─ 文档分块
   ├─ 向量化（Embedding）
   └─ 存入向量数据库

2. 检索阶段
   ├─ 用户问题向量化
   ├─ 在向量库中检索
   └─ 获取最相关的文档块

3. 生成阶段
   ├─ 将检索结果和用户问题组合
   ├─ 构建提示词
   └─ LLM 生成回答
```

### 2.2 流程图示

```
用户问题 → 向量化 → 向量检索 → 相关文档 → 构建上下文 → LLM 生成 → 回答
```

## 3. 关键技术

### 3.1 文档分块

**为什么分块？**
- 文档太长，不适合直接存入
- 检索时需要粒度适中的内容

**分块策略：**
- 固定大小（如 512 Token）
- 按段落分割
- 按语义分割

### 3.2 向量化（Embedding）

将文本转换为向量。

**常用 Embedding 模型：**
- OpenAI text-embedding-ada-002
- sentence-transformers
- Cohere Embeddings

### 3.3 向量数据库

存储向量并支持相似度检索。

**常用向量数据库：**
- Chroma（轻量，本地）
- Pinecone（云服务）
- Weaviate
- Qdrant
- Milvus

## 4. 在当前项目中的应用

### 4.1 简单实现示例

```python
# 伪代码示例
from vector_db import VectorDB
from embedding import Embedder
from llm import LLM

# 1. 准备数据
documents = load_documents()
chunks = split_documents(documents)

# 2. 向量化并存库
embeddings = Embedder.encode(chunks)
db = VectorDB()
db.add(chunks, embeddings)

# 3. 检索
query = "用户问题"
query_embedding = Embedder.encode(query)
results = db.search(query_embedding, top_k=5)

# 4. 生成
context = "\n\n".join(results)
prompt = f"基于以下信息回答：\n{context}\n问题：{query}"
answer = LLM.generate(prompt)
```

### 4.2 最佳实践

| 实践 | 说明 |
|------|------|
| **合理分块** | 选择合适的分块大小和策略 |
| **质量 Embedding** | 使用高质量的 Embedding 模型 |
| **检索优化** | 调整 top_k、重排序等 |
| **上下文整合** | 有效地将检索结果整合到提示词中 |

### 4.3 注意事项

- 注意：分块大小影响效果
- 注意：检索质量决定最终质量
- 注意：需要处理检索不到的情况
- 注意：注意成本和效率的平衡

## 5. 总结

RAG 详解要点：
- ✅ 理解 RAG 的概念和作用
- ✅ 掌握完整的工作流程
- ✅ 了解关键技术：分块、向量化、向量数据库
- ✅ 在项目中实现 RAG 系统
- ✅ 持续优化检索和生成质量

:::tip 下一步
接下来学习 [检索优化技术](./04-检索优化技术.md)！
:::
