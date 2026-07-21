 OpenAgent Studio

> AI Agent 桌面应用 —— 上传文档、AI 问答、自动化报告

## 项目简介

OpenAgent Studio 是一个集成了 RAG 知识库、AI 对话、Agent 工作流的桌面应用。

## 技术栈

| 模块 | 技术 |
|------|------|
| 后端 | Python, FastAPI |
| 前端 | Streamlit + pywebview |
| 数据库 | MySQL, SQLAlchemy |
| AI | Ollama, DeepSeek API, LangChain |
| Agent | LangGraph, MCP |
| 部署 | Docker, docker-compose |

## 功能

- 用户系统（注册/登录/JWT 认证）
- AI 多轮对话（支持多模型切换）
- RAG 知识库（上传 PDF/Word）
- Agent 工作台（单 Agent + 多 Agent 协作）
- MCP 工具集（Excel 分析 + Word 报告）
- Docker 一键部署

## 快速开始

`ash
git clone https://github.com/RINGO88-lab/openagent-studio.git
cd openagent-studio
pip install -r requirements.txt
python run.py
`

## 项目迭代

| 版本 | 功能 |
|------|------|
| V0.1 | 控制台用户管理 |
| V0.2 | 模块化重构 + JSON 持久化 |
| V1.0 | Web 版 + 数据库 + JWT |
| V2.0 | AI 聊天 |
| V3.0 | RAG + Agent |
| V4.0 | 多 Agent + MCP |
