from pprint import pprint
import requests
import pytest
import yaml
from pathlib import Path
from config import API_LOGIN

DATA_DIR = Path(__file__).parent / "data"

def load_login_cases():
    with open(DATA_DIR / "login_data.yml", encoding="utf-8") as f:
        cases = yaml.safe_load(f)
        # pprint(cases["cases"])
        return cases["cases"]

@pytest.mark.parametrize("case", load_login_cases())
def test_login(base_url,case):
    url = f"{base_url}{API_LOGIN}"

    resp = requests.post(url,
                         json={"username":case["username"],
                               "password":case["password"]},
                         timeout=5)

    data = resp.json()
    assert data["code"] == case["expect_code"]


