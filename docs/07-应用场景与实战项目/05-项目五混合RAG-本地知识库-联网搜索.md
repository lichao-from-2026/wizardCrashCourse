---
title: 混合 RAG Agent：本地知识库 + 联网搜索合并回答
description: 实现 Agent 模式，合并本地知识和网络搜索结果，适合专业领域（如分子生物学）
author: AI Agent 知识库团队
date: 2026-04-24
category: 应用场景与实战项目
---

# 混合 RAG Agent：本地知识库 + 联网搜索合并回答

本文教你构建一个**智能 Agent**，它能根据问题自动决定：
- 只查本地知识库？
- 只联网搜索？
- 两者合并？

特别适合**分子生物学**等专业领域！

---

## 1. 技术架构

### 1.1 整体流程

```
用户问题
    ↓
┌─────────────────────────────────────┐
│         智能 Agent                    │
│  思考：这个问题需要什么信息？          │
│  - 问题在不在我的本地知识库？         │
│  - 需要最新网络信息吗？                │
└──────────┬──────────────────────────┘
           ↓
    ┌──────┴──────┐
    ↓             ↓
本地 RAG        联网搜索
    ↓             ↓
    └──────┬──────┘
           ↓
    合并信息 + LLM → 最终回答
```

### 1.2 技术选型

| 组件 | 技术 | 说明 |
|------|------|------|
| **本地 LLM** | Ollama | llama3.1:8b 或 qwen2.5:7b |
| **本地知识库** | LlamaIndex + Chroma | 管理你的专业文档 |
| **网络搜索** | DuckDuckGo (免费) 或 Serper API | 联网获取最新信息 |
| **Agent 框架** | LlamaIndex Query Pipeline / Agent | 智能决策 |

---

## 2. 环境准备

### 2.1 安装依赖

```bash
# 基础依赖
pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama llama-index-vector-stores-chroma python-dotenv

# 联网搜索
pip install duckduckgo-search

# 或者用 Serper API（推荐，效果更好）
# 去 https://serper.dev 注册，获取免费 API Key
```

### 2.2 拉取模型

```bash
ollama pull llama3.1:8b
ollama pull nomic-embed-text:latest
```

---

## 3. 完整代码实现

### 3.1 项目结构

```
hybrid_rag_agent/
├── data/                    # 你的专业文档（分子生物学论文、笔记）
│   ├── paper1.md
│   └── ...
├── storage/                 # 索引（自动生成）
├── agent.py                 # 完整 Agent 代码
├── build_index.py           # 构建索引
└── .env                     # 配置
```

### 3.2 构建索引（build_index.py）

```python
# build_index.py
import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore

load_dotenv()

Settings.llm = Ollama(model="llama3.1:8b", request_timeout=60.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")

PERSIST_DIR = "./storage"
DATA_DIR = "./data"

def build_index():
    print(f"正在从 {DATA_DIR} 加载文档...")
    documents = SimpleDirectoryReader(DATA_DIR).load_data()
    print(f"加载了 {len(documents)} 个文档块")
    
    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("hybrid_rag")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    print("正在创建索引...")
    index = VectorStoreIndex.from_documents(
        documents, 
        storage_context=storage_context,
        show_progress=True
    )
    
    index.storage_context.persist(persist_dir=PERSIST_DIR)
    print(f"索引已保存到 {PERSIST_DIR}")
    return index

def load_index():
    if not os.path.exists(PERSIST_DIR):
        return build_index()
    
    print(f"正在从 {PERSIST_DIR} 加载索引...")
    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("hybrid_rag")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(
        persist_dir=PERSIST_DIR,
        vector_store=vector_store
    )
    
    index = load_index_from_storage(storage_context)
    return index

if __name__ == "__main__":
    build_index()
```

### 3.3 混合 Agent 完整代码（agent.py）

```python
# agent.py
import os
from dotenv import load_dotenv
from typing import List, Dict
from llama_index.core import Settings, QueryBundle
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker, AgentRunner
from llama_index.core.postprocessor import SimilarityPostprocessor
from duckduckgo_search import DDGS
from build_index import load_index

load_dotenv()

Settings.llm = Ollama(model="llama3.1:8b", request_timeout=60.0, temperature=0.7)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")

index = load_index()
local_query_engine = index.as_query_engine(similarity_top_k=3)

def web_search(query: str, num_results: int = 3) -> str:
    """使用 DuckDuckGo 进行网络搜索，获取最新信息
    
    Args:
        query: 搜索关键词
        num_results: 返回结果数量
        
    Returns:
        搜索结果的文本摘要
    """
    print(f"🌐 正在网络搜索: {query}")
    results = DDGS().text(query, max_results=num_results)
    if not results:
        return "未找到网络搜索结果"
    
    summaries = []
    for i, r in enumerate(results, 1):
        summaries.append(f"[结果 {i}] {r['title']}\n{r['body']}\n")
    return "\n".join(summaries)

def query_local_knowledge_base(question: str) -> str:
    """查询本地知识库（你的专业文档、笔记、论文）
    
    Args:
        question: 用户的问题
        
    Returns:
        本地知识库的回答及来源
    """
    print(f"📚 正在查询本地知识库: {question}")
    response = local_query_engine.query(question)
    
    result = f"回答: {response.response}\n\n来源:\n"
    for i, node in enumerate(response.source_nodes, 1):
        score = node.score or 0.0
        result += f"{i}. (相似度: {score:.2f})\n{node.node.get_content()[:400]}...\n"
    return result

web_search_tool = FunctionTool.from_defaults(fn=web_search)
local_kb_tool = FunctionTool.from_defaults(fn=query_local_knowledge_base)

system_prompt = """
你是一个专业的研究助手 Agent，特别是在分子生物学等专业领域有专长。

你的任务是根据用户的问题，智能决定使用哪些工具：

规则：
1. 如果问题涉及**用户的个人笔记、本地文档、上传的论文**，首先调用 `query_local_knowledge_base`
2. 如果问题需要**最新信息、研究进展、新闻、实时数据**，调用 `web_search`
3. 如果问题既需要本地知识又需要网络信息，两个工具都调用，然后合并回答
4. 回答时要清晰标注信息来源（本地知识库 vs 网络搜索）
5. 回答要专业、准确、有参考文献意识

你可以同时调用多个工具！
"""

agent_worker = FunctionCallingAgentWorker.from_tools(
    [web_search_tool, local_kb_tool],
    llm=Settings.llm,
    system_prompt=system_prompt,
    verbose=True
)
agent = AgentRunner(agent_worker)

def ask_agent(question: str):
    print(f"\n🤔 用户问题: {question}\n")
    print("="*80)
    response = agent.chat(question)
    print("="*80)
    print(f"\n✨ 最终回答:\n{response.response}")
    return response

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("请输入你的问题: ")
    
    ask_agent(question)
```

---

## 4. 使用步骤

### 4.1 准备你的专业文档

```
hybrid_rag_agent/
└── data/
    ├── 2025-01-15-CRISPR-Cas9-review.md   ← 你的分子生物学论文
    ├── lab-notes.md                       ← 实验笔记
    └── ...
```

### 4.2 构建索引

```bash
python build_index.py
```

### 4.3 运行 Agent 查询

```bash
# 例 1：只涉及本地知识
python agent.py "我的笔记里关于 CRISPR-Cas9 的原理是什么？"

# 例 2：需要网络最新信息
python agent.py "2025年最新的基因编辑研究进展有哪些？"

# 例 3：两者都要
python agent.py "结合我的笔记和最新研究，CRISPR 在治疗遗传病方面有什么新进展？"
```

---

## 5. 分子生物学专属最佳实践

### 5.1 文档准备建议

| 文档类型 | 建议 |
|---------|------|
| **PDF 论文** | 用 Marker 或 PyMuPDF 转成 Markdown，保留公式和表格 |
| **实验数据** | 转成 Markdown 表格，方便检索 |
| **专业术语** | 文档中保持术语统一，必要时加简短定义 |
| **OCR** | 如果有图片图表，先转文本 |

### 5.2 推荐文档格式（分子生物学）

```markdown
# 2025-01-15 CRISPR-Cas9 综述笔记

## 核心原理
CRISPR-Cas9 是一种基因编辑技术，利用导向 RNA (gRNA) 引导 Cas9 酶到目标 DNA 序列。

## 关键组分
| 组分 | 功能 |
|-----|------|
| Cas9 酶 | 切割 DNA |
| gRNA | 引导到目标位置 |
| 修复模板 | HDR 修复用 |

## 实验流程
1. 设计 gRNA
2. 构建载体
3. 转染细胞
4. 检测编辑效率
```

### 5.3 进阶：更好的搜索工具（Serper API）

如果 DuckDuckGo 效果不够好，推荐用 Serper API：

```python
# 替换 web_search 函数
import requests

def web_search_serper(query: str, num_results: int = 5):
    """使用 Serper API 搜索（效果更好）"""
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        return "请配置 SERPER_API_KEY"
    
    url = "https://google.serper.dev/search"
    payload = {"q": query, "num": num_results}
    headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    results = response.json()
    
    summaries = []
    if "organic" in results:
        for i, r in enumerate(results["organic"][:num_results], 1):
            summaries.append(f"[{i}] {r.get('title', '')}\n{r.get('snippet', '')}\n")
    return "\n".join(summaries)
```

---

## 6. Streamlit Web 界面

```python
# app.py
import streamlit as st
from agent import ask_agent, Settings, Ollama

st.set_page_config(page_title="混合 RAG Agent", page_icon="🧬", layout="wide")

st.title("🧬 混合 RAG Agent - 本地知识库 + 联网搜索")
st.markdown("智能 Agent 自动决定查本地还是联网，特别适合专业领域研究！")

st.sidebar.title("⚙️ 设置")
model_option = st.sidebar.selectbox("选择模型", ["llama3.1:8b", "qwen2.5:7b"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
Settings.llm = Ollama(model=model_option, temperature=temperature, request_timeout=60.0)

question = st.text_input("❓ 输入你的问题:", placeholder="例如：结合我的笔记和最新研究，CRISPR有什么新进展？")

if question:
    with st.spinner("🤔 Agent 正在思考..."):
        try:
            response = ask_agent(question)
            st.markdown("### ✨ 回答")
            st.info(response.response)
        except Exception as e:
            st.error(f"错误: {e}")
```

---

## 7. 常见问题

### Q: 分子生物学的专业术语能理解吗？
A: 可以！只要：
1. 你的本地文档里有这些术语的上下文
2. 用合适的 Embedding 模型
3. 必要时联网搜索补充最新解释

### Q: PDF 论文效果如何？
A: 建议转成 Markdown，效果更好。纯 PDF 可能会有排版问题。

### Q: 如何确保 Agent 正确调用工具？
A: 调整 `system_prompt`，给更明确的指示。

---

## 8. 总结

本文介绍了：
- ✅ 混合 RAG Agent 架构
- ✅ 本地知识库 + 联网搜索合并回答
- ✅ 分子生物学专业领域的最佳实践
- ✅ 完整代码和 Web 界面

现在你可以拥有一个既能查你的私人笔记，又能获取网络最新研究的智能助手了！
