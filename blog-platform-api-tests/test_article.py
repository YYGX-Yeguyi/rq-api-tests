import uuid

from config import *
import requests

def test_get_article_list(base_url):
    """测试：获取文章列表"""
    url = base_url + API_ARTICLE_LIST

    response = requests.get(url, timeout=TIMEOUT)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 200
    assert "data" in resp_json
    assert "records" in resp_json["data"]

    print(f"获取文章列表测试通过，共 {len(resp_json['data']['records'])} 篇文章")


def test_get_article_detail(base_url):
    """测试：获取文章详情（使用存在的文章ID）"""
    # 先用 1 作为测试文章ID，实际应该从列表接口获取
    article_id = 2
    url = base_url + f"{API_ARTICLE_DETAIL}/{article_id}"

    response = requests.get(url, timeout=TIMEOUT)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 200
    assert "data" in resp_json
    assert resp_json["data"]["id"] == article_id

    print(f"获取文章详情测试通过，文章ID: {article_id}")


def test_get_article_detail_not_exist(base_url):
    """测试：获取不存在的文章详情"""
    article_id = 99999
    url = base_url + f"{API_ARTICLE_DETAIL}/{article_id}"

    response = requests.get(url, timeout=TIMEOUT)

    resp_json = response.json()
    # 不存在的文章，返回 code 应该不是 200
    assert resp_json["code"] != 200

    print(f"获取不存在的文章测试通过")


def test_create_article_with_auth(login_token, base_url):
    """测试：创建文章（需要登录），跑完清理掉自己创建的文章"""
    # 1. 先登录获取 token fix:使用fixture获取token
    #token = test_login_success()

    # 2. 创建文章
    url = base_url + API_ARTICLE_SAVE
    headers = {"Authorization": f"Bearer {login_token}"}

    # 唯一标题：save 返回 data 为空，创建后按标题反查 id 用于清理
    unique_title = f"【pytest fixture】测试文章-{uuid.uuid4().hex[:6]}"
    article_data = {
        "title": unique_title,
        "content": "这是通过 fixture 获取 token 创建",
        "summary": " fixture 测试",
        "categoryId": 1,
        "status": 1
    }

    created_id = None
    try:
        response = requests.post(url, json=article_data, headers=headers, timeout=TIMEOUT)

        assert response.status_code == 200, "请求发送成功"
        resp_json = response.json()
        assert resp_json["code"] == 200, "业务请求成功"

        # 反查刚创建文章的 id
        list_resp = requests.get(
            base_url + API_ARTICLE_LIST,
            params={"page": 1, "size": 50},
            timeout=TIMEOUT,
        ).json()
        matched = [r["id"] for r in list_resp["data"]["records"] if r["title"] == unique_title]
        assert matched, f"按唯一标题未找到刚创建的文章:{unique_title}"
        created_id = matched[0]

        print("创建文章测试通过")
    finally:
        # 无论断言是否失败，都清理掉刚创建的文章，避免污染数据库
        if created_id is not None:
            delete_resp = requests.delete(
                base_url + API_ARTICLE_DELETE + f"/{created_id}",
                headers=headers,
                timeout=TIMEOUT,
            ).json()
            assert delete_resp["code"] in (200, 404), f"清理测试文章失败:{delete_resp}"


def test_create_article_without_auth(base_url):
    """测试：未登录创建文章（应该失败）"""
    url = base_url + API_ARTICLE_SAVE

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

    print(f"未登录创建文章测试通过（正确拒绝）")


def test_delete_article_with_auth(login_token,base_url,article_id):
    url = base_url + API_ARTICLE_DELETE
    headers = {
        "Authorization": f"Bearer {login_token}"
    }
    response = requests.delete(f"{url}/{article_id}", headers=headers, timeout=TIMEOUT)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["code"] == 200

def test_delete_article_without_auth(base_url):
    url = base_url + API_ARTICLE_DELETE
    # 不存在的 id：后端未登录时先校验 token 返回 401，不会真正删除任何文章
    article_id = 999999

    response = requests.delete(f"{url}/{article_id}", timeout=TIMEOUT)
    assert response.status_code == 401
    assert response.json()["code"] == 401



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