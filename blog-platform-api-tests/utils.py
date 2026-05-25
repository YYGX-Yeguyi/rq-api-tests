import json
import os


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

