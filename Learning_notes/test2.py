# @Time :2019/7/31 22:32
# @Author :jinbiao

import requests

class OperationRequest:
    """
    发送接口请求
    """
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, data, is_json=False):
        if method == "get":
            res = self.session.get(url=url, param=data)
        elif method == "post":
            if is_json:
                res = self.session.post(url=url, json=data)
            else:
                res = self.session.post(url=url, data=data)
        return res


if __name__ == '__main__':
    login_url = "http://tj.lemonban.com/futureloan/mvc/api/member/login"
    param = {"mobilephone": 13611767797, "pwd": "test1234"}
    op = OperationRequest()
    res = op.send_request(method="post", url=login_url, data=param)
    print(res.text)


