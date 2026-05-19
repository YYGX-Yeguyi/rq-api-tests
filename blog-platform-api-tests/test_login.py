import requests
from config import BASE_URL,TIMEOUT,API_LOGIN
from utils import load_test_data

#加载测试数据
test_data = load_test_data("test_data.json")
#定义不同的测试用例的函数
#成功
def test_login_success():
    '''
        1.拼接地址
        2.找出json数据中的成功的数据
        3.response 获取回复
        4.断言判断 status_code 网络请求是否发送成功
        5.将响应json数据转化为字典,判断业务状态 code 是否正确6
        6.先断言data在断言token
        7.最后输出成功登录,并返回token的值给其他请求使用
    '''
    #拼接地址
    url = BASE_URL + API_LOGIN
    data = test_data["login"]["valid_user"]

    #发送
    response = requests.post(url,json=data,timeout=TIMEOUT)

    # 断言
    assert response.status_code == 200, f"HTTP状态码错误：{response.status_code}"

    resp_json = response.json()
    assert resp_json["code"] == 200, f"业务状态码错误：{resp_json['code']}"
    assert "data" in resp_json, "返回数据中没有data字段"
    assert "token" in resp_json["data"], "返回数据中没有token"

    print("登录成功测试通过")
    return resp_json["data"]["token"]  # 返回 token 供后续使用

#错误的密码

#不存在的用户

#最后执行手动后测试

