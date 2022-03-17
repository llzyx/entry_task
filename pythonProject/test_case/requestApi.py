#请求接口
import requests
import json
from variable import url
class requestApi():
    def module(self,param):
        header={'Content-Type':'application/json'}
        res_obj=requests.get(url=url,data=json.dumps(param),headers=header)
        return res_obj.json()


if __name__=='__main__':
    re=requestApi()
    re.module({
    "a":1,
    "b":"bbb",
    "c":1
})