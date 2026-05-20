from os import name

import requests
from config import BASE_URL,API_CATEGORY_LIST

def test_category_list():
    #拼接地址
    url = BASE_URL+API_CATEGORY_LIST
    #发送get请求
    response = requests.get(url)
    assert response.status_code == 200,"请求失败"
    #获取返回的数据
    resp_json = response.json()
    print(resp_json)
    #判断返回是否正确
    assert resp_json["code"] == 200,f"业务错误{resp_json['code']}"
    assert "data" in resp_json,"返回的数据中没有data"
    assert isinstance(resp_json["data"],list),"data不是列表"

    #有数据的话,判断数据的结构是否正确
    if len (resp_json["data"]) > 0:
        first_category = resp_json["data"][0]
        assert "id" in first_category, "分类数据中没有id"
        assert "name" in first_category, "分类数据中没有name"
    clist = resp_json["data"]
    print(f"成功通过测试,有{len(resp_json["data"])}个分类,"
          f"分别是{clist[0]['name']},{clist[1]['name']},{clist[2]['name']}")

    return None