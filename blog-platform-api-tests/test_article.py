import requests
from config import *
from test_login import test_login_success


def test_get_article_list():
    """测试：获取文章列表"""
    url = BASE_URL + API_ARTICLE_LIST

    response = requests.get(url, timeout=TIMEOUT)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 200
    assert "data" in resp_json
    assert "records" in resp_json["data"]

    print(f"✅ 获取文章列表测试通过，共 {len(resp_json['data']['records'])} 篇文章")


def test_get_article_detail():
    """测试：获取文章详情（使用存在的文章ID）"""
    # 先用 1 作为测试文章ID，实际应该从列表接口获取
    article_id = 2
    url = BASE_URL + f"{API_ARTICLE_DETAIL}/{article_id}"

    response = requests.get(url, timeout=TIMEOUT)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 200
    assert "data" in resp_json
    assert resp_json["data"]["id"] == article_id

    print(f"✅ 获取文章详情测试通过，文章ID: {article_id}")


def test_get_article_detail_not_exist():
    """测试：获取不存在的文章详情"""
    article_id = 99999
    url = BASE_URL + f"{API_ARTICLE_DETAIL}/{article_id}"

    response = requests.get(url, timeout=TIMEOUT)

    resp_json = response.json()
    # 不存在的文章，返回 code 应该不是 200
    assert resp_json["code"] != 200

    print(f"✅ 获取不存在的文章测试通过")


def test_create_article_with_auth():
    """测试：创建文章（需要登录）"""
    # 1. 先登录获取 token
    token = test_login_success()

    # 2. 创建文章
    url = BASE_URL + API_ARTICLE_SAVE
    headers = {"Authorization": f"Bearer {token}"}

    article_data = {
        "title": "【自动化测试】测试文章",
        "content": "这是通过自动化脚本创建的文章内容",
        "summary": "自动化测试摘要",
        "categoryId": 1,
        "status": 1
    }

    response = requests.post(url, json=article_data, headers=headers, timeout=TIMEOUT)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 200

    print(f"✅ 创建文章测试通过")


def test_create_article_without_auth():
    """测试：未登录创建文章（应该失败）"""
    url = BASE_URL + API_ARTICLE_SAVE

    article_data = {
        "title": "未登录创建的文章",
        "content": "不应该成功",
        "categoryId": 1,
        "status": 1
    }

    response = requests.post(url, json=article_data, timeout=TIMEOUT)

    # 未认证应该返回 401 或 403，或者业务 code 不是 200
    resp_json = response.json()
    # 根据你的 API 设计，可能返回 code=401 或 status_code=401
    assert resp_json["code"] != 200 or response.status_code == 401

    print(f"✅ 未登录创建文章测试通过（正确拒绝）")


if __name__ == "__main__":
    print("=" * 50)
    print("开始测试文章接口")
    print("=" * 50)

    test_get_article_list()
    test_get_article_detail()
    test_get_article_detail_not_exist()
    test_create_article_without_auth()
    test_create_article_with_auth()

    print("=" * 50)
    print("所有文章测试完成")
    print("=" * 50)