# rq-api-tests 个人 API 自动化测试项目

<div align="center">

<!-- 第一行 -->
![Python Version](https://img.shields.io/badge/Python-3.14-blue)
![pytest](https://img.shields.io/badge/pytest-9.0-blue)
![Requests](https://img.shields.io/badge/Requests-2.32-blue)

<!-- 第二行 -->
![Test Cases](https://img.shields.io/badge/测试用例-14个-brightgreen)
![Pass Rate](https://img.shields.io/badge/通过率-100%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

## 项目简介

本项目是对个人开发的博客平台后端 API 进行的接口自动化测试。基于 **Python + Pytest + Requests** 构建，覆盖用户登录、分类管理、文章管理等核心模块，实现了测试数据与代码分离、session 级 token 共享、多环境切换以及 HTML / Allure 报告自动生成等功能。

## 基本数据

| 项目       | 数据   |
| ---------- | ------ |
| 测试文件数 | 4 个   |
| 测试用例数 | 14 个  |
| 通过率     | 100%   |
| 执行时间   | 约 1 秒 |

### 测试覆盖范围

| 模块     | 接口                  | 测试场景                                         | 用例数 |
| -------- | --------------------- | ------------------------------------------------ | ------ |
| 用户管理 | `/api/auth/login`     | 成功登录、密码错误、用户不存在（函数式 + 数据驱动） | 6      |
| 分类管理 | `/api/category/list`  | 获取分类列表                                     | 1      |
| 文章管理 | `/api/article/list`   | 获取文章列表                                     | 1      |
| 文章管理 | `/api/article/detail` | 获取文章详情、不存在的文章                       | 2      |
| 文章管理 | `/api/article/save`   | 认证创建文章、未认证创建文章                     | 2      |
| 文章管理 | `/api/article/delete` | 认证删除文章、未认证删除文章                     | 2      |

## 项目目录结构

```
rq-api-tests/                              # 项目根目录
├── blog-platform-api-tests/               # 测试主目录
│   ├── conftest.py                        # pytest 配置（session 级 token、--env 参数、base_url）
│   ├── pytest.ini                         # pytest 配置（HTML + Allure 报告）
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
├── .gitignore                             # Git 忽略文件
├── requirements.txt                       # 项目依赖
└── README.md                              # 项目说明
```

## 技术栈

| 类别      | 工具               | 用途                 |
| :-------- | :----------------- | :------------------- |
| 编程语言  | Python 3.14        | 主要开发语言         |
| 测试框架  | Pytest 9.0         | 测试用例管理与执行   |
| HTTP 请求 | Requests 2.32      | 发送 HTTP 请求       |
| 数据驱动  | PyYAML 6.0         | 解析 YAML 测试数据   |
| 报告生成  | pytest-html 4.2    | 生成 HTML 测试报告   |
| 报告生成  | allure-pytest 2.16 | 生成 Allure 报告     |
| 版本控制  | Git                | 代码版本管理         |

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

切换环境时使用 `--env` 参数（默认 `dev`）：

```bash
pytest                          # 默认 dev 环境
pytest --env=test               # 测试环境
pytest --env=prod               # 生产环境
```

### 4. 运行测试

```bash
# 运行所有测试
pytest

# 运行指定测试文件
pytest testcases/test_login.py -v -s

# 运行指定测试用例
pytest testcases/test_article.py::test_get_article_list -v -s
```

> 已在 `pytest.ini` 中配置默认报告输出：HTML 报告生成到 `reports/report.html`，Allure 结果生成到 `allure-results/`。

### 5. 查看报告

```bash
# 打开 HTML 报告
start reports/report.html

# 生成并查看 Allure 报告（需先安装 allure 命令行工具）
allure serve allure-results
```

## 测试结果示例

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

## 项目亮点

1. **Session 级 Token 共享**：整个测试过程只登录一次，所有需要认证的测试共享同一个 token
2. **数据驱动**：测试数据与代码分离，支持 JSON 与 YAML 两种格式，修改数据无需改动代码
3. **模块化分层**：按 `config` / `common` / `data` / `testcases` 标准分层，请求统一由 `api_client` 封装
4. **自动化报告**：每次测试自动生成 HTML 与 Allure 双报告，便于结果分析
5. **多环境切换**：通过 `--env` 参数在 dev / test / prod 之间切换，登录与业务请求统一指向同一环境
6. **自动清理**：文章创建 / 删除用例通过唯一标题反查并自动清理测试数据，避免污染数据库

## 后续计划

- [ ] 集成 GitHub Actions，实现 CI/CD 自动测试
- [ ] 增加更多边界值测试用例
- [ ] 增加日志模块，便于问题排查

## 作者

阮乾 | [GitHub](https://github.com/YYGX-Yeguyi)
