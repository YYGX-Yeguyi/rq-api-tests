from pprint import pprint
import requests
import pytest
import yaml
from pathlib import Path
from common.api_client import *

from config.settings import *

DATA_DIR = Path(__file__).parent.parent / "data"

def load_login_cases():
    with open(DATA_DIR / "login_data.yml", encoding="utf-8") as f:
        cases = yaml.safe_load(f)
        # pprint(cases["cases"])
        return cases["cases"]

@pytest.mark.parametrize("case", load_login_cases())
def test_login(base_url,case):
    url = f"{base_url}{API_LOGIN}"

    resp = post(url,
                         json={"username":case["username"],
                               "password":case["password"]},
                         )

    data = resp.json()
    assert data["code"] == case["expect_code"]


