import uuid

import pytest

from common.api_client import *
from config.settings import *
from common.utils import load_test_data

test_data = load_test_data("test_data.json")

@pytest.fixture(scope="session")
def article_id(login_token, base_url):
    # 唯一标题：save 返回 data 为空拿不到 id，靠唯一标题反查，避免同秒创建时"查最新"拿错
    unique_title = f"【临时】删除用例专用文章-{uuid.uuid4().hex[:6]}"
    url = base_url + API_ARTICLE_SAVE
    body = {
        "title": unique_title,
        "content": "# 测试正文",
        "summary": "用于删除测试，跑完自动清理",
        "categoryId": 1,
        "status": 1,
        "isTop": 0,
    }
    resp = post(url,body,login_token).json()
    assert resp['code'] == 200, f"创建文章失败:{resp}"

    list_resp = get(
        base_url + API_ARTICLE_LIST,
        params={"page": 1, "size": 50}
    ).json()
    matched = [r["id"] for r in list_resp["data"]["records"] if r["title"] == unique_title]
    assert matched, f"按唯一标题未找到临时文章:{unique_title}"
    aid = matched[0]

    yield aid

    delete_url = base_url + API_ARTICLE_DELETE + f"/{aid}"
    delete_resp = delete(delete_url,login_token).json()
    # 200=本次清理成功；404=用例已删除该文章，无需重复清理
    assert delete_resp["code"] in (200, 404), f"清理虚拟文章失败:{delete_resp}"

@pytest.fixture(scope="session")#整个测试过程只执行一次
def login_token(base_url):
    url = base_url + API_LOGIN
    json = test_data["login"]["valid_user"]
    response = post(url,json)
    resp = response.json()
    #断言是非登录成功
    assert resp["code"]==200,"登录失败"
    assert "token"  in resp["data"],"返回数据没有token"
    #断言返回是否有token

    token = resp["data"]["token"]

    print(f"\n [conftest] 获取token成功,token:{token:30}")
    return token

def pytest_addoption(parser):
    """添加自定义命令行参数 --env"""
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=("dev", "test", "prod"),
        help="运行环境: dev(默认), test, prod"
    )
@pytest.fixture(scope="session")
def env(request):
    """返回当前环境名称"""
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_url(env):
    """根据环境返回不同的 BASE_URL"""
    urls = {
        "dev": "http://localhost:8080",
        "test": "http://47.116.30.242:8080",
        "prod": "http://47.116.30.242:8080"   # 改成你真实的生产地址
    }
    return urls[env]