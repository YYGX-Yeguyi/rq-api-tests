# rq-api-tests 个人 API 自动化测试项目

# 

<div align="center">


<!-- 第一行 -->
![Python Version](https://img.shields.io/badge/Python-3.14-blue)
![pytest](https://img.shields.io/badge/pytest-9.0-blue)
![Requests](https://img.shields.io/badge/Requests-2.32-blue)

<!-- 第二行 -->
![Test Cases](https://img.shields.io/badge/测试用例-9个-brightgreen)
![Pass Rate](https://img.shields.io/badge/通过率-100%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

## 项目简介

本项目是对个人开发的博客平台后端 API 进行的接口自动化测试。基于 **Python + Pytest + Requests** 构建，覆盖用户登录、分类管理、文章管理等核心模块，实现了测试数据与代码分离、session 级 token 共享、HTML 报告自动生成等功能。

## 基本数据

| 项目       | 数据   |
| ---------- | ------ |
| 测试文件数 | 3 个   |
| 测试用例数 | 9 个   |
| 通过率     | 100%   |
| 执行时间   | 0.8 秒 |

### 测试覆盖范围

| 模块     | 接口                  | 测试场景                       | 用例数 |
| -------- | --------------------- | ------------------------------ | ------ |
| 用户管理 | `/api/auth/login`     | 成功登录、密码错误、用户不存在 | 3      |
| 分类管理 | `/api/category/list`  | 获取分类列表                   | 1      |
| 文章管理 | `/api/article/list`   | 获取文章列表                   | 1      |
| 文章管理 | `/api/article/detail` | 获取文章详情、不存在的文章     | 2      |
| 文章管理 | `/api/article/save`   | 认证创建文章、未认证创建文章   | 2      |

## 项目目录结构

```
rq-api-tests/                                 # 项目根目录
├── blog-platform-api-tests/                  # 博客平台测试目录
│   ├── conftest.py                           # pytest 配置（session 级 token）
│   ├── config.py                             # 环境配置（URL、API 路径）
│   ├── utils.py                              # 工具函数（请求封装、数据加载）
│   ├── test_data.json                        # 测试数据
│   ├── test_login.py                         # 登录接口测试（3 个用例）
│   ├── test_category.py                      # 分类接口测试（1 个用例）
│   ├── test_article.py                       # 文章接口测试（5 个用例）
│   ├── pytest.ini                            # pytest 配置文件
│   └── reports/                              # 测试报告目录
│       └── report.html                       # HTML 测试报告
├── .gitignore                                # Git 忽略文件
├── requirements.txt                          # 项目依赖
└── README.md                                 # 项目说明
```



------

## 技术栈

| 类别      | 工具            | 用途               |
| :-------- | :-------------- | :----------------- |
| 编程语言  | Python 3.14     | 主要开发语言       |
| 测试框架  | Pytest 9.0      | 测试用例管理与执行 |
| HTTP 请求 | Requests 2.32   | 发送 HTTP 请求     |
| 报告生成  | pytest-html 4.2 | 生成 HTML 测试报告 |
| 版本控制  | Git             | 代码版本管理       |

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/YYGX-Yeguyi/rq-api-tests.git
cd rq-api-tests/blog-platform-api-tests
```

### 2. 安装依赖

```bash
pip install -r ../requirements.txt
```

### 3. 配置后端地址

修改 `config.py` 中的 `BASE_URL`：

```python
BASE_URL = "http://localhost:8080"   # 改成你的后端地址
```

### 4. 运行测试

```bash
# 进入测试目录
cd blog-platform-api-tests

# 运行所有测试
pytest

# 运行指定文件
pytest test_login.py -v -s

# 生成 HTML 报告
pytest --html=reports/report.html --self-contained-html
```

## 测试结果示例

```bash
collected 9 items

test_article.py::test_get_article_list PASSED
test_article.py::test_get_article_detail PASSED
test_article.py::test_get_article_detail_not_exist PASSED
test_article.py::test_create_article_with_auth PASSED
test_article.py::test_create_article_without_auth PASSED
test_category.py::test_category_list PASSED
test_login.py::test_login_success PASSED
test_login.py::test_login_FPassword PASSED
test_login.py::test_login_Fusername PASSED

======================= 9 passed in 0.78s ========================
```

## 修改 Bug 记录

### Bug #1：测试数据文件路径问题
- **现象**：`FileNotFoundError: test_data.json`
- **原因**：相对路径依赖当前工作目录
- **解决**：使用 `os.path.dirname(__file__)` 动态获取路径

### Bug #2：登录接口 415 错误
- **现象**：返回 `415 Unsupported Media Type`
- **原因**：后端只接受表单格式，代码用了 `json=data`
- **解决**：改为 `data=data`

### Bug #3：测试函数返回非 None
- **现象**：pytest 警告 `PytestReturnNotNoneWarning`
- **原因**：测试函数中使用了 `return`
- **解决**：删除 `return`，测试函数应返回 `None`

### Bug #4：分类数量硬编码
- **现象**：代码写死 `clist[0]`、`clist[1]`、`clist[2]`
- **原因**：假设始终有 3 个分类
- **解决**：动态遍历分类列表

### Bug #5：每个测试都重复登录
- **现象**：每个需要 token 的测试都单独调用登录接口
- **原因**：没有使用 pytest fixture 共享 token
- **解决**：创建 `conftest.py`，使用 `@pytest.fixture(scope="session")`

## 项目亮点

1. **Session 级 Token 共享**：整个测试过程只登录一次，所有需要认证的测试共享同一个 token
2. **数据驱动**：测试数据与代码分离，修改数据无需改动代码
3. **模块化设计**：按功能拆分测试文件，通过 `conftest.py` 统一管理配置
4. **自动化报告**：每次测试自动生成 HTML 报告，便于结果分析
5. **版本控制**：代码托管于 GitHub，支持团队协作

## 后续计划

- [ ] 集成 GitHub Actions，实现 CI/CD 自动测试
- [ ] 增加更多边界值测试用例
- [ ] 支持多环境配置切换（dev/test/prod）
- [ ] 增加日志模块，便于问题排查

## 作者

阮乾 | [GitHub](https://github.com/YYGX-Yeguyi)

