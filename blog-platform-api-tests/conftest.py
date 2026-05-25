import pytest
import requests
from config import TIMEOUT,API_LOGIN,BASE_URL
from utils import load_test_data

test_data = load_test_data("test_data.json")
@pytest.fixture(scope="session")#整个测试过程只执行一次
def login_token():
    url = BASE_URL + API_LOGIN
    data = test_data["login"]["valid_user"]
    response = requests.post(url,json=data,timeout=TIMEOUT)
    resp = response.json()

    #断言是非登录成功
    assert resp["code"]==200,"登录失败"
    assert "token"  in resp["data"],"返回数据没有token"
    #断言返回是否有token

    token = resp["data"]["token"]

    print(f"/n [conftest] 获取token成功,token:{token:30}")
    return token

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

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
        "test": "http://test.blog-platform.com",
        "prod": "https://http://47.116.30.242:8080"   # 改成你真实的生产地址
    }
    return urls[env]