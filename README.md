# 给migangbot用的一些api

一个用于提供多种游戏市场数据的REST API。

## 功能特点

- 查询各种游戏的物品市场数据
- 模块化架构，易于扩展到其他游戏/市场

## FFXIV市场API

- 查询任何可交易的FFXIV物品数据
- 可过滤只显示高品质(HQ)物品
- 数据来源：[Universalis](https://universalis.app/)

### GET /api/ffxiv/get_market_data

获取特定服务器上特定物品的市场数据。

**参数：**

- `server_name` (字符串，必填)：要查询的服务器名称（例如："Moogle"，"红玉海"）
- `item_name` (字符串，必填)：要搜索的物品名称
- `hq` (布尔值，可选，默认为false)：是否只过滤高品质物品

**示例响应：**

```json
{
  "status": "success",
  "data": "红玉海 的 白银锭 数据如下：\n10,000x10 = 100,000   RetainerName\n11,000x5 = 55,000   RetainerName2\n...\n更新时间:2023-09-01 12:34:56"
}
```

## 项目结构

```
market-api/
├── .github/                 # GitHub配置
│   └── workflows/           # GitHub Actions工作流
│       └── docker-publish.yml # Docker构建与发布配置
├── ffxiv/                   # FFXIV相关代码
│   ├── __init__.py          # 包初始化
│   ├── market.py            # 市场数据函数
│   └── routes.py            # FFXIV的API路由
├── main.py                  # 应用入口点
├── requirements.txt         # Python依赖
├── Dockerfile               # Docker构建文件
└── README.md                # 本文件
```

## 安装与设置

### 本地运行

1. 克隆仓库
2. 安装依赖
```
pip install -r requirements.txt
```
3. 运行API服务器
```
python main.py
```

API将在 http://localhost:8000 可用

### Docker部署

#### 从DockerHub拉取镜像

```
docker pull 用户名/migangbot-api:latest
docker run -d -p 8000:8000 用户名/migangbot-api:latest
```

#### 本地构建

1. 构建Docker镜像
```
docker build -t migangbot-api .
```

2. 运行Docker容器
```
docker run -d -p 8000:8000 migangbot-api
```

API将在 http://localhost:8000 可用

## CI/CD

本项目使用GitHub Actions自动构建和部署Docker镜像到DockerHub。

### 如何设置

1. 在GitHub仓库设置中添加以下Secrets:
   - `DOCKERHUB_USERNAME`: DockerHub用户名
   - `DOCKERHUB_TOKEN`: DockerHub访问令牌（在DockerHub账户设置中创建）

2. 配置完成后，每当推送到main分支或创建新的版本标签(v*.*.*)时，GitHub Actions将自动:
   - 构建Docker镜像
   - 将镜像推送到DockerHub仓库
   - 根据分支名或标签名标记镜像

### 手动触发构建

你也可以在GitHub仓库的Actions页面手动触发工作流。

## 文档

API文档在服务器运行时自动生成，可在 http://localhost:8000/docs 访问。