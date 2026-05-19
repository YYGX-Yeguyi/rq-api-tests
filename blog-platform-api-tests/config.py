# config.py
# 配置文件：存放环境相关的配置
# 基础 URL
BASE_URL = "http://localhost:8080"

# API 路径
API_LOGIN = "/api/auth/login"
API_CATEGORY_LIST = "/api/category/list"
API_ARTICLE_LIST = "/api/article/list"
API_ARTICLE_DETAIL = "/api/article/detail"
API_ARTICLE_SAVE = "/api/article/save"
API_ARTICLE_DELETE = "/api/article/delete"

# 请求超时时间（秒）
TIMEOUT = 10