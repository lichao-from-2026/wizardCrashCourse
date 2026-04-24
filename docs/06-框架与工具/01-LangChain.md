---
title: LangChain
description: 最流行的 LLM 应用开发框架
author: AI Agent 知识库团队
date: 2026-04-24
category: 框架与工具
---

# 一、LangChain

LangChain 是目前最流行的 LLM 应用开发框架！它通过模块化设计，让开发者可以快速构建复杂的 LLM 应用。

## 1. 什么是 LangChain

### 1.1 定义

LangChain 是一个用于开发由语言模型驱动的应用程序的框架。它的核心思想是将 LLM 与各种计算资源和数据源链接（chain）在一起。

### 1.2 与传统框架的区别

| 特性 | 传统 Web 框架 | LangChain |
|------|--------------|-----------|
| **核心驱动** | 数据库 + 业务逻辑 | LLM 推理 + 工具调用 |
| **状态管理** | 显式、可预测 | 隐式、依赖 LLM 输出 |
| **执行流程** | 确定的控制流 | 动态的推理链 |
| **错误处理** | 可预期的异常 | 需要容错和重试 |
| **数据来源** | 结构化数据 | 非结构化文本 + 多种数据源 |

## 2. 核心概念详解

### 2.1 核心组件

| 概念 | 说明 | 类比 |
|------|------|------|
| **LLM** | 大语言模型封装 | 大脑 |
| **Prompt Template** | 提示词模板 | 脚本模板 |
| **Chain** | 多个组件链接在一起 | 流水线 |
| **Agent** | 具有推理和工具调用能力 | 智能助手 |
| **Memory** | 记忆系统 | 短期/长期记忆 |
| **Retriever** | 检索器（RAG） | 搜索引擎 |

### 2.2 整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                         LangChain 应用                          │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────────────────┐  ┌──────────────┐  │
│  │  Memory  │  │       Agent          │  │  Retriever   │  │
│  │  (记忆)  │  │     (推理决策)       │  │   (RAG)     │  │
│  └────┬─────┘  └──────────┬───────────┘  └───────┬──────┘  │
│       │                   │                     │         │
│       └───────────────────┼─────────────────────┘         │
│                           │                               │
│  ┌─────────────────────────┼─────────────────────────────┐│
│  │                         │                             ││
│  │   ┌───────────────────┐ │  ┌───────────────────────┐  ││
│  │   │  Prompt Template │ │  │   Chain (链式调用)    │  ││
│  │   │   (提示词模板)   │ │  │  (串联多个组件)       │  ││
│  │   └───────────┬───────┘ │  └───────────┬───────────┘  ││
│  │               │         │             │              ││
│  │   ┌───────────┴───────┐ │  ┌───────────┴───────────┐  ││
│  │   │      LLM         │ │  │      Tools            │  ││
│  │   │  (大语言模型)    │ │  │    (工具/API调用)     │  ││
│  │   └───────────────────┘ │  └───────────────────────┘  ││
│  └──────────────────────────┴─────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## 3. 原理与使用思路

### 3.1 LangChain 的核心原理

**1. 模块化设计**
- 将复杂应用拆分为独立组件
- 每个组件专注一件事
- 组件可以自由组合

**2. 链式调用（Chaining）**
- 一个组件的输出作为下一个组件的输入
- 构建数据流动的管道
- 支持同步和异步执行

**3. 推理-行动循环**
- LLM 决定下一步做什么
- 执行相应的工具/函数
- 根据结果继续推理

### 3.2 使用思路

```
Step 1: 定义输入/输出
  ↓
Step 2: 选择合适的组件
  ↓
Step 3: 构建链条/Agent
  ↓
Step 4: 测试和调试
  ↓
Step 5: 优化和扩展
```

## 4. 基础语法与 API

### 4.1 安装与配置

```bash
pip install langchain langchain-openai python-dotenv
```

**基础配置**

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)
```

### 4.2 简单调用示例

```python
response = llm.invoke("请写一首关于编程的短诗")
print(response.content)
```

## 5. 核心模块详细案例

### 5.1 案例 1：Prompt Template（提示词模板）

```python
from langchain.prompts import ChatPromptTemplate

# 创建提示词模板
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一位专业的{profession}。请用简洁明了的语言回答。"),
    ("user", "{question}")
])

# 渲染提示词
formatted_prompt = prompt_template.format(
    profession="Python 开发者",
    question="什么是装饰器？"
)

print(formatted_prompt)
```

**将模板与 LLM 链接**

```python
from langchain_core.output_parsers import StrOutputParser

# 创建 Chain
chain = prompt_template | llm | StrOutputParser()

# 执行 Chain
result = chain.invoke({
    "profession": "Python 开发者",
    "question": "什么是装饰器？"
})

print(result)
```

### 5.2 案例 2：Memory（记忆系统）

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# 创建带记忆的对话链
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# 多轮对话
response1 = conversation.predict(input="我叫小明")
print(response1)

response2 = conversation.predict(input="我叫什么名字？")
print(response2)  # 记住了"小明"
```

**更强大的记忆类型**

```python
from langchain.memory import ConversationSummaryMemory

# 摘要记忆（适合长对话）
summary_memory = ConversationSummaryMemory.from_messages(
    llm=llm,
    return_messages=True
)
```

### 5.3 案例 3：RAG（检索增强生成）

```python
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# 1. 加载文档
loader = TextLoader("data/knowledge.txt")
documents = loader.load()

# 2. 分割文档
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
docs = text_splitter.split_documents(documents)

# 3. 创建向量存储
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(
    docs, 
    embeddings,
    persist_directory="./chroma_db"
)

# 4. 创建 RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

# 5. 提问
query = "我们公司的产品有什么特点？"
result = qa_chain.invoke({"query": query})

print("回答：", result["result"])
print("\n来源文档：", [doc.page_content for doc in result["source_documents"]])
```

### 5.4 案例 4：Agent（智能代理）

```python
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain.tools import tool

# 1. 定义工具
search = DuckDuckGoSearchRun()
wikipedia = WikipediaQueryRun()

@tool
def calculate(expression: str) -> str:
    """计算数学表达式，例如 '2 + 2 * 3'"""
    try:
        return str(eval(expression))
    except:
        return "计算错误"

tools = [search, wikipedia, calculate]

# 2. 创建提示词
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能助手，可以使用多种工具来回答问题。"),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# 3. 创建 Agent
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 4. 执行
result = agent_executor.invoke({
    "input": "2024年奥运会在哪个城市举办？那个城市的人口有多少？"
})

print(result["output"])
```

### 5.5 案例 5：完整实战 - 文档问答助手

```python
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema.runnable import RunnablePassthrough

# 1. 准备知识库（同案例3）
# 假设 db 已经初始化好了

# 2. 创建自定义提示词
template = """仅使用以下上下文来回答问题。
如果你不知道答案，就说不知道，不要编造答案。

{context}

问题：{question}

请用中文回答。
"""

custom_prompt = PromptTemplate.from_template(template)

# 3. 构建完整 Chain
def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

rag_chain = (
    {"context": db.as_retriever() | format_docs, "question": RunnablePassthrough()}
    | custom_prompt
    | llm
    | StrOutputParser()
)

# 4. 使用
response = rag_chain.invoke("什么是 RAG 系统？")
print(response)
```

## 6. 优势与劣势

### 6.1 优势

- ✅ **生态丰富**：大量集成组件，开箱即用
- ✅ **社区活跃**：文档完善，问题易解决
- ✅ **灵活组合**：模块化设计，按需组装
- ✅ **多模型支持**：OpenAI、Anthropic、开源模型均可
- ✅ **多语言**：TypeScript/JS 也有对应版本

### 6.2 劣势

- ⚠️ **学习曲线陡峭**：概念较多
- ⚠️ **抽象层可能过重**：简单应用可能觉得复杂
- ⚠️ **版本迭代快**：API 变化较频繁
- ⚠️ **调试较困难**：复杂链的调试需要技巧

## 7. 适用场景

### 7.1 最适合

- 🎯 RAG 系统
- 🎯 聊天机器人
- 🎯 工作流自动化
- 🎯 多 Agent 协作
- 🎯 数据分析助手

### 7.2 不适合

- ❌ 超简单的单轮问答（直接调 API 即可）
- ❌ 对性能要求极高的生产系统
- ❌ 需要完全控制底层的场景

## 8. 最佳实践

### 8.1 开发最佳实践

| 实践 | 说明 |
|------|------|
| **从小开始** | 先构建简单的 Chain，再逐步添加组件 |
| **充分测试** | 每个组件独立测试后再集成 |
| **合理使用 Memory** | 根据场景选择合适的记忆类型 |
| **错误处理** | 预期 LLM 可能犯错，做好异常处理 |
| **监控迭代** | 记录运行日志，持续优化提示词 |

### 8.2 性能优化

```python
# 使用缓存
from langchain.cache import InMemoryCache
import langchain

langchain.llm_cache = InMemoryCache()

# 使用流式输出
for chunk in llm.stream("写一篇关于AI的文章"):
    print(chunk.content, end="", flush=True)
```

## 9. 实际项目模板

```python
# my_rag_app.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

class RAGApplication:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.embeddings = OpenAIEmbeddings()
        self.db = None
        self.chain = None
    
    def load_knowledge_base(self, persist_dir: str):
        self.db = Chroma(
            persist_directory=persist_dir,
            embedding_function=self.embeddings
        )
    
    def build_chain(self):
        template = """使用以下上下文回答问题。
上下文: {context}
问题: {question}
"""
        prompt = PromptTemplate.from_template(template)
        
        def format_docs(docs):
            return "\n\n".join([d.page_content for d in docs])
        
        self.chain = (
            {
                "context": self.db.as_retriever(search_kwargs={"k": 3}) | format_docs,
                "question": RunnablePassthrough()
            }
            | prompt
            | self.llm
            | StrOutputParser()
        )
    
    def query(self, question: str) -> str:
        return self.chain.invoke(question)

# 使用示例
if __name__ == "__main__":
    app = RAGApplication()
    app.load_knowledge_base("./chroma_db")
    app.build_chain()
    
    answer = app.query("什么是 LangChain？")
    print(answer)
```

## 10. 总结

LangChain 是入门 Agent 开发的绝佳选择！它提供了：

- 🔧 丰富的组件生态
- 🧩 灵活的组合方式
- 📚 完善的文档和社区
- 🎯 快速构建复杂应用的能力

对于任何想要构建 LLM 应用的开发者来说，LangChain 都是一个值得深入学习和掌握的框架。

::: tip 下一步
接下来学习 [CrewAI](./02-CrewAI.md)，看看多 Agent 协作框架！
:::
