#参数a的取值
import pytest
from requestApi import requestApi
from variable import a,b
import allure


@allure.feature('参数a的值小于0')
def test_a():
    param={'a':a[0],'b':b[0]}
    re = requestApi().module(param)
    assert re['code'] == 21, '返回错误码不正确'
    assert re['message'] == 'empty or wrong params', '返回message不正确'
    assert re['reference'] == f'a={param.get("a")},b={param.get("b")}', '返回reference不正确'

@allure.feature('参数a的值等于0')
def test_b():
    param = {'a': a[1],'b':b[0]}
    re = requestApi().module(param)
    assert re['code'] == 21, '返回错误码不正确'
    assert re['message'] == 'empty or wrong params', '返回message不正确'
    assert re['reference'] == f'a={param.get("a")},b={param.get("b")}', '返回reference不正确'

@allure.feature('参数a的值大于0')
def test_c():
    param = {'a': a[2],'b':b[0]}
    re = requestApi().module(param)
    assert re['code'] == 0, '返回错误码不正确'
    assert re['message'] == 'success', '返回message不正确'
    assert re['reference'] == f'a={param.get("a")},b={param.get("b")}', '返回reference不正确'

if __name__=='__main__':
    pytest.main(["-sv","test_paramA.py"])