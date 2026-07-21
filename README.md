# AI 股票分析助手

> 桌面级 AI 股票分析工具 —— 实时行情、AI 分析、Agent 日报、交易行为诊断

## 项目简介

一款集成行情数据、AI 智能分析、RAG 财报解析、Agent 自动化日报、个人交易行为诊断的桌面股票分析工具。

## 技术栈

| 模块 | 技术 |
|------|------|
| 后端 | Python, FastAPI |
| 前端 | Streamlit + pywebview（桌面端） |
| 数据 | akshare（行情）、爬虫（新闻） |
| 可视化 | mplfinance, Plotly |
| 数据库 | MySQL, SQLAlchemy |
| 缓存 | Redis |
| AI | DeepSeek API, LangChain |
| RAG | LangChain + ChromaDB（财报解析） |
| Agent | LangGraph（日报/复盘自动化） |
| 部署 | Docker, docker-compose, Linux |
| 工程 | Git, Pytest, asyncio, WebSocket |

## 功能

### 行情与图表
- 自选股管理 + 实时行情（akshare 接入东方财富）
- K 线图（日/周/月） + MACD/RSI/KDJ 技术指标
- 分时图 + 板块资金流向

### AI 智能分析
- 新闻舆情分析（爬取新闻 + AI 利好利空判断）
- 财报 PDF 解析（RAG 提取营收/利润/毛利率等指标）
- AI 综合评分（基本面 + 技术面 + 舆情面）
- AI 买卖参考（结合技术形态 + 策略回测胜率）

### Agent 自动化
- 早报 Agent（开盘前抓新闻 + AI 分析 + 推送）
- 复盘 Agent（收盘后自动分析当日走势）

### 个人交易行为分析（核心亮点）
- 导入券商交割单（PDF/Excel 解析）
- 胜率 / 盈亏比 / 最大回撤统计
- 错误行为识别：追涨杀跌、扛单、卖飞
- AI 改进建议

### 持仓与预警
- 投资组合管理（持仓/盈亏/收益率）
- 策略回测（验证买卖策略的历史表现）
- 预警系统（涨跌 / 金叉死叉 / 异动提醒）

## 快速开始

`
git clone https://github.com/RINGO88-lab/ai-stock-assistant.git
cd ai-stock-assistant
docker-compose up
`

## 项目结构

`
ai-stock-assistant/
├── backend/
│   ├── api/           # FastAPI 接口
│   ├── services/      # AI / RAG / Agent 逻辑
│   ├── data/          # 数据获取（akshare/爬虫）
│   └── models/        # 数据库模型
├── frontend/          # Streamlit 界面
├── docs/
└── docker-compose.yml
`
