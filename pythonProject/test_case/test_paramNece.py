#校验缺少\增加参数
import pytest
from requestApi import requestApi
from variable import a,b
import allure

@allure.feature('缺少参数a')
def test_a():
    param={"b":b[0]}
    re=requestApi().module(param)
    assert re['code']==0,'返回错误码不正确'
    assert re['message']=='success','返回message不正确'
    assert re['reference']==f'a={param.get("a")},b={param.get("b")}','返回reference不正确'

@allure.feature('缺少参数b')
def test_b():
    param={"a":a[2]}
    re = requestApi().module(param)
    assert re['code'] == 21, '返回错误码不正确'
    assert re['message'] == 'empty or wrong params', '返回message不正确'
    assert re['reference'] == f'a={param.get("a")},b={param.get("b")}', '返回reference不正确'

@allure.feature('增加多余参数c')
def test_c():
    param = {"a": a[2],'b':b[0],'c':1}
    re = requestApi().module(param)
    assert re['code'] == 0, '返回错误码不正确'
    assert re['message'] == 'success', '返回message不正确'
    assert re['reference'] == f'a={param.get("a")},b={param.get("b")}', '返回reference不正确'

if __name__=='__main__':
    pytest.main(["-sv","test_paramNece.py"])
