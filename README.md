# rq-api-tests 个人博客平台自动化测试项目

<div align="center">

<!-- 第一行 -->
![Python Version](https://img.shields.io/badge/Python-3.14-blue)
![pytest](https://img.shields.io/badge/pytest-9.0-blue)
![Requests](https://img.shields.io/badge/Requests-2.34-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.63-blue)

<!-- 第二行 -->
![API Tests](https://img.shields.io/badge/接口测试-14个-brightgreen)
![UI Tests](https://img.shields.io/badge/UI测试-2个-brightgreen)
![Test Cases](https://img.shields.io/badge/测试用例-16个-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

## 项目简介

本项目是对个人开发的博客平台进行的两层自动化测试，包含 **接口自动化测试** 与 **UI 自动化测试** 两套独立的测试套件：

- **接口测试**：基于 **Python + Pytest + Requests**，覆盖用户登录、分类管理、文章管理等核心模块，实现了测试数据与代码分离、session 级 token 共享、多环境切换以及 HTML / Allure 报告自动生成。
- **UI 测试**：基于 **Playwright**，覆盖页面正常渲染、后台登录跳转等场景，并接入 GitHub Actions 实现自动执行与失败截图。

## 基本数据

| 项目       | 数据     |
| ---------- | -------- |
| 接口测试文件数 | 4 个   |
| 接口测试用例数 | 14 个  |
| UI 测试文件数  | 2 个   |
| UI 测试用例数  | 2 个   |
| 测试用例总数   | 16 个  |
| 执行时间   | 接口约 1 秒，UI 视环境而定 |

### 接口测试覆盖范围

| 模块     | 接口                  | 测试场景                                         | 用例数 |
| -------- | --------------------- | ------------------------------------------------ | ------ |
| 用户管理 | `/api/auth/login`     | 成功登录、密码错误、用户不存在（函数式 + 数据驱动） | 6      |
| 分类管理 | `/api/category/list`  | 获取分类列表                                     | 1      |
| 文章管理 | `/api/article/list`   | 获取文章列表                                     | 1      |
| 文章管理 | `/api/article/detail` | 获取文章详情、不存在的文章                       | 2      |
| 文章管理 | `/api/article/save`   | 认证创建文章、未认证创建文章                     | 2      |
| 文章管理 | `/api/article/delete` | 认证删除文章、未认证删除文章                     | 2      |

### UI 测试覆盖范围

| 模块     | 页面                  | 测试场景               | 用例数 |
| -------- | --------------------- | ---------------------- | ------ |
| 首页     | `/`                    | 页面正常渲染（标题可见） | 1      |
| 登录     | `/login`               | 正确账号密码登录跳转后台 | 1      |

## 项目目录结构

```
rq-api-tests/                              # 项目根目录
├── blog-platform-api-tests/               # 接口自动化测试主目录
│   ├── conftest.py                        # pytest 配置（session 级 token、--env 参数、base_url）
│   ├── pytest.ini                         # pytest 配置（HTML + Allure 报告）
│   ├── requirements.txt                   # 接口测试依赖
│   ├── config/
│   │   └── settings.py                    # 环境配置（API 路径、超时时间）
│   ├── common/
│   │   ├── api_client.py                  # 请求封装（get / post / delete）
│   │   └── utils.py                       # 工具函数（测试数据加载）
│   ├── data/
│   │   ├── test_data.json                 # 测试数据（JSON）
│   │   └── login_data.yml                 # 登录测试数据（YAML 数据驱动）
│   ├── testcases/
│   │   ├── test_login.py                  # 登录接口测试（3 个用例）
│   │   ├── test_login_data.py             # 登录接口数据驱动测试（3 个用例）
│   │   ├── test_category.py               # 分类接口测试（1 个用例）
│   │   └── test_article.py                # 文章接口测试（7 个用例）
│   ├── reports/                           # HTML 测试报告
│   └── allure-results/                    # Allure 报告数据
├── blog-ui-tests/                         # UI 自动化测试主目录
│   ├── conftest.py                        # pytest 配置
│   ├── requirements.txt                   # UI 测试依赖
│   ├── pages/
│   │   └── test_ui_home.py                # 首页渲染测试（1 个用例）
│   └── testcases/
│       └── test_ui_login.py               # 登录跳转测试（1 个用例）
├── .github/
│   └── workflows/
│       ├── api-test.yml                   # 接口测试 CI（push / PR 自动触发）
│       └── ui-test.yml                    # UI 测试 CI（手动触发）
├── .gitignore                             # Git 忽略文件
├── requirements.txt                       # 项目依赖（汇总）
└── README.md                              # 项目说明
```

## 技术栈

| 类别      | 工具               | 用途                 |
| :-------- | :----------------- | :------------------- |
| 编程语言  | Python 3.14        | 主要开发语言         |
| 测试框架  | Pytest 9.0         | 测试用例管理与执行   |
| HTTP 请求 | Requests 2.34      | 发送 HTTP 请求       |
| UI 自动化 | Playwright 1.63    | 浏览器自动化测试     |
| 数据驱动  | PyYAML 6.0         | 解析 YAML 测试数据   |
| 报告生成  | pytest-html 4.2    | 生成 HTML 测试报告   |
| 报告生成  | allure-pytest 2.16 | 生成 Allure 报告     |
| CI/CD     | GitHub Actions     | 自动执行测试         |
| 版本控制  | Git                | 代码版本管理         |

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/YYGX-Yeguyi/rq-api-tests.git
cd rq-api-tests
```

### 2. 安装依赖

```bash
# 接口测试依赖
pip install -r blog-platform-api-tests/requirements.txt

# UI 测试依赖（含浏览器驱动）
pip install -r blog-ui-tests/requirements.txt
playwright install chromium
```

### 3. 配置后端地址（接口测试）

环境地址统一在 `conftest.py` 的 `base_url` fixture 中维护，通过 `--env` 参数切换：

```python
@pytest.fixture(scope="session")
def base_url(env):
    urls = {
        "dev": "http://localhost:8080",        # 本地开发环境
        "test": "http://47.116.30.242:8080",   # 测试服务器
        "prod": "http://47.116.30.242:8080"    # 改成你真实的生产地址
    }
    return urls[env]
```

### 4. 运行接口测试

```bash
cd blog-platform-api-tests

# 运行所有测试（默认 dev 环境）
pytest

# 切换环境
pytest --env=test
pytest --env=prod

# 运行指定测试文件
pytest testcases/test_login.py -v -s

# 运行指定测试用例
pytest testcases/test_article.py::test_get_article_list -v -s
```

> 已在 `pytest.ini` 中配置默认报告输出：HTML 报告生成到 `reports/report.html`，Allure 结果生成到 `allure-results/`。

### 5. 运行 UI 测试

UI 测试需要前端项目运行在本地的 `http://localhost:5173`（登录跳转用例依赖后端服务）。

```bash
cd blog-ui-tests

# 运行所有 UI 测试（headless=False 可看到浏览器）
pytest -v
```

### 6. 查看报告

```bash
# 打开 HTML 报告
start blog-platform-api-tests/reports/report.html

# 生成并查看 Allure 报告（需先安装 allure 命令行工具）
allure serve blog-platform-api-tests/allure-results
```

## 持续集成（GitHub Actions）

项目已配置两套 CI 工作流：

| 工作流       | 触发方式              | 内容                                       |
| ------------ | --------------------- | ------------------------------------------ |
| `api-test.yml` | push / PR 到 main     | 在 `test` 环境运行接口测试，上传 Allure 结果 |
| `ui-test.yml`  | 手动触发（`workflow_dispatch`） | 运行 UI 测试，失败时上传截图   |

## 测试结果示例

接口测试：

```bash
collected 14 items

testcases/test_article.py::test_get_article_list PASSED
testcases/test_article.py::test_get_article_detail PASSED
testcases/test_article.py::test_get_article_detail_not_exist PASSED
testcases/test_article.py::test_create_article_with_auth PASSED
testcases/test_article.py::test_create_article_without_auth PASSED
testcases/test_article.py::test_delete_article_with_auth PASSED
testcases/test_article.py::test_delete_article_without_auth PASSED
testcases/test_category.py::test_category_list PASSED
testcases/test_login.py::test_login_success PASSED
testcases/test_login.py::test_login_FPassword PASSED
testcases/test_login.py::test_login_Fusername PASSED
testcases/test_login_data.py::test_login[case0] PASSED
testcases/test_login_data.py::test_login[case1] PASSED
testcases/test_login_data.py::test_login[case2] PASSED

======================= 14 passed in 0.8s ========================
```

UI 测试：

```bash
collected 2 items

pages/test_ui_home.py::test_home_shows_page PASSED
testcases/test_ui_login.py::test_admin_login PASSED

======================= 2 passed in 3.2s ========================
```

## 项目亮点

1. **两层测试覆盖**：接口测试 + UI 测试双管齐下，既校验后端契约，也校验前端交互
2. **Session 级 Token 共享**：整个接口测试过程只登录一次，所有需要认证的测试共享同一个 token
3. **数据驱动**：测试数据与代码分离，支持 JSON 与 YAML 两种格式，修改数据无需改动代码
4. **模块化分层**：接口测试按 `config` / `common` / `data` / `testcases` 标准分层，请求统一由 `api_client` 封装
5. **自动化报告**：接口测试自动生成 HTML 与 Allure 双报告，便于结果分析
6. **多环境切换**：通过 `--env` 参数在 dev / test / prod 之间切换，登录与业务请求统一指向同一环境
7. **自动清理**：文章创建 / 删除用例通过唯一标题反查并自动清理测试数据，避免污染数据库
8. **CI/CD 集成**：接口测试推送即自动执行，UI 测试手动触发并自动保存失败截图

## 后续计划

- [ ] 增加更多边界值测试用例
- [ ] 增加日志模块，便于问题排查
- [ ] UI 测试接入数据驱动与页面对象（Page Object）模式
- [ ] 为 UI 测试接入 Allure 报告

## 作者

阮乾 | [GitHub](https://github.com/YYGX-Yeguyi)
