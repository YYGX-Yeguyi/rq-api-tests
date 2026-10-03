import json
from pathlib import Path


# utils.py 在 common/ 下，向上跳一层到项目根，再进 data
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_test_data(file_name):
    """加载 data/ 目录下的 JSON 测试数据"""
    with open(DATA_DIR / file_name, "r", encoding="utf-8") as f:
        return json.load(f)


def get_token_from_login_response(response):
    data = response.json()
    if data.get("code") == 200 and data.get("data"):
        return data["data"].get("token")
    return None