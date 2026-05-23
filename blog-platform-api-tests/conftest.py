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

