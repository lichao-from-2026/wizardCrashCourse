---
title: LlamaIndex - 知识库 RAG 专家
description: 专注于知识库和 RAG 系统的强大框架
author: AI Agent 知识库团队
date: 2026-04-24
category: 框架与工具
---

# LlamaIndex - 知识库 RAG 专家

LlamaIndex（原 GPT Index）是**专为知识库和 RAG 系统设计**的框架！它让复杂的知识管理变得简单高效。

## 1. 什么是 LlamaIndex

### 1.1 核心理念

LlamaIndex 专注于解决一个问题：**如何将你的私有数据连接到 LLM**

- 📚 **数据连接** - 支持 100+ 数据源
- 🔍 **智能索引** - 优化检索效果
- 🤖 **查询引擎** - 高级问答能力
- 🔧 **灵活扩展** - 可高度定制

### 1.2 LlamaIndex vs LangChain

| 维度 | LlamaIndex | LangChain |
|------|-----------|-----------|
| **设计目标** | 知识库、RAG 专家 | 通用 LLM 应用框架 |
| **学习曲线** | 较平缓 | 较陡峭 |
| **RAG 能力** | ⭐⭐⭐⭐⭐ 专业级 | ⭐⭐⭐⭐ 优秀 |
| **灵活性** | 中等 | 极高 |
| **生态覆盖** | 专注知识库 | 全面覆盖 |

---

## 2. 核心概念

### 2.1 核心组件

| 组件 | 作用 |
|------|------|
| **Document** | 原始文档（PDF、Markdown 等） |
| **Node** | 文档分割后的小块 |
| **Index** | 索引（Vector、Tree 等） |
| **Retriever** | 检索器，从索引中找相关文档 |
| **Query Engine** | 查询引擎，回答问题 |
| **Response Synthesizer** | 响应合成器，组合信息生成答案 |

### 2.2 工作流程

```
原始文档 → 文档加载 → 文档分割 → 向量化 → 索引存储
                                                ↓
用户查询 → 查询向量化 → 相似性检索 → 上下文组装 → LLM 回答
```

---

## 3. 快速入门

### 3.1 安装

```bash
pip install llama-index llama-index-llms-openai
```

### 3.2 最简示例

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

# 配置
Settings.llm = OpenAI(model="gpt-4o", temperature=0.7)

# 1. 加载文档
documents = SimpleDirectoryReader("data").load_data()

# 2. 创建索引
index = VectorStoreIndex.from_documents(documents)

# 3. 查询
query_engine = index.as_query_engine()
response = query_engine.query("这篇文档讲了什么？")

print(response)
```

---

## 4. 本地模型实战 (Ollama)

### 4.1 配置 Ollama

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings

# 配置本地 LLM
Settings.llm = Ollama(
    model="llama3.1:8b",
    request_timeout=60.0
)
Settings.embed_model = OllamaEmbedding(
    model_name="nomic-embed-text:latest"
)
```

### 4.2 完整本地知识库代码

```python
from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader,
    StorageContext, 
    load_index_from_storage
)
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
import os.path

# 配置
Settings.llm = Ollama(model="llama3.1:8b", request_timeout=60.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")

PERSIST_DIR = "./storage"

if not os.path.exists(PERSIST_DIR):
    # 首次：创建索引
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # 加载已有索引
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# 查询
query_engine = index.as_query_engine()
response = query_engine.query("介绍一下这个项目")
print(response)
```

---

## 5. 高级功能

### 5.1 多种索引类型

```python
from llama_index.core import (
    VectorStoreIndex,          # 向量索引（推荐）
    TreeIndex,                # 树状索引
    KeywordTableIndex,        # 关键词索引
    SummaryIndex             # 摘要索引
)

# 向量索引（最常用）
index = VectorStoreIndex.from_documents(documents)

# 树状索引（层级检索）
index = TreeIndex.from_documents(documents)
```

### 5.2 自定义文档分割

```python
from llama_index.core.node_parser import SentenceSplitter

Settings.text_splitter = SentenceSplitter(
    chunk_size=512,       # 每个块大小
    chunk_overlap=100    # 块之间的重叠
)
```

### 5.3 高级查询模式

```python
# 1. 流式查询
query_engine = index.as_query_engine(streaming=True)
response = query_engine.query("请详细说明")
for text in response.response_gen:
    print(text, end="")

# 2. 检索 + 合成模式（分开）
retriever = index.as_retriever(similarity_top_k=5)
nodes = retriever.retrieve("问题")

# 3. 聊天引擎
chat_engine = index.as_chat_engine()
response = chat_engine.chat("你好")
response = chat_engine.chat("基于文档回答")
```

### 5.4 混合检索

```python
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=5
)

query_engine = RetrieverQueryEngine(
    retriever=retriever,
    node_postprocessors=[
        SimilarityPostprocessor(similarity_cutoff=0.7)
    ]
)
```

---

## 6. 向量数据库集成

### 6.1 Chroma（本地推荐）

```python
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext

# 初始化 Chroma
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("my_collection")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# 创建存储上下文
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 创建索引
index = VectorStoreIndex.from_documents(
    documents, 
    storage_context=storage_context
)
```

### 6.2 其他向量数据库

LlamaIndex 支持各种流行的向量数据库：
- Chroma - 本地轻量
- Pinecone - 云端托管
- Weaviate - 开源强大
- Milvus / Zilliz - 企业级
- Qdrant - 高性能

---

## 7. 最佳实践

### 7.1 知识库构建建议

| 步骤 | 建议 |
|------|------|
| **文档格式** | Markdown > PDF > Word |
| **Chunk Size** | 512-1024 tokens |
| **Overlap** | 50-150 tokens |
| **检索数量** | Top 3-5 |

### 7.2 性能优化

```python
# 1. 使用更快的 Embedding 模型
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")

# 2. 缓存结果
from llama_index.core import set_global_handler
set_global_handler("simple")

# 3. 并行处理
index = VectorStoreIndex.from_documents(
    documents, 
    show_progress=True,
    use_async=True
)
```

### 7.3 提示词优化

```python
from llama_index.core import PromptTemplate

# 自定义 QA 提示词
qa_prompt_tmpl = PromptTemplate("""
使用以下上下文信息回答问题。
如果你不知道答案，就说不知道，不要编造。

上下文：
{context_str}

问题：{query_str}

请用中文回答：
""")

query_engine = index.as_query_engine(
    text_qa_template=qa_prompt_tmpl
)
```

---

## 8. 实战场景

### 8.1 场景一：个人知识库

- 文档格式：Markdown、PDF、笔记
- 部署：本地 Ollama + Streamlit
- 特点：隐私、免费、无 API 费用

### 8.2 场景二：企业文档系统

- 数据源：Confluence、Notion、GitHub
- 部署：云端托管 + 向量数据库
- 特点：多人协作、权限控制

### 8.3 场景三：研究论文助手

- 数据：Arxiv、PDF 论文
- 功能：文献检索、问答、总结
- 特点：专业领域知识

---

## 9. 总结

LlamaIndex 是：

- ✅ **RAG 专家** - 专为知识库设计
- ✅ **简单高效** - 少量代码完成复杂功能
- ✅ **数据源丰富** - 支持 100+ 数据格式
- ✅ **本地支持** - 完美搭配 Ollama 等本地模型
- ✅ **灵活扩展** - 可定制化程度高

对于知识库和 RAG 系统，LlamaIndex 是最佳选择！

::: tip 下一步
查看"项目四：个人本地知识库"，获得完整实战代码！
:::
