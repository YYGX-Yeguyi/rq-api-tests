from email.header import Header

import requests
import json
import os

from openai import base_url

from config import BASE_URL,TIMEOUT

def post(url,data=None,headers=None,need_auth=False,token=None):
    """
       封装 POST 请求
       :param url: 接口路径
       :param data: 请求体（JSON）
       :param headers: 请求头
       :param need_auth: 是否需要认证
       :param token: token
       :return: response 对象
       """
    full_url = BASE_URL + url
    req_headers = headers or {}
    if need_auth and token:
        req_headers['Authorization'] = f'Bearer {token}'

    # 发送请求 fix:修正缩进,代码问题
    response = requests.post(full_url, json=data, headers=req_headers, timeout=TIMEOUT)
    return response

def get(url, need_auth=False, token=None):
    """
    封装 GET 请求
    """
    full_url = base_url + url

    headers = {}
    if need_auth and token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(full_url, headers=headers, timeout=TIMEOUT)
    return response

def delete(url, need_auth=False, token=None):
    """
    封装 DELETE 请求
    """
    full_url = BASE_URL + url

    headers = {}
    if need_auth and token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.delete(full_url, headers=headers, timeout=TIMEOUT)
    return response


def load_test_data(file_name):
    """
    加载 JSON 测试数据
    """
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_token_from_login_response(response):
    data = response.json()
    if data["code"]==200 and "data" in data:
        return data["data"]["token"]
    return None

