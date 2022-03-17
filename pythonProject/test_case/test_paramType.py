#校验参数类型
import pytest
from requestApi import requestApi
from variable import a,b
import allure

@allure.feature('参数类型错误')
@pytest.mark.parametrize("param",[{'a':a[3],'b':b[0]},{'a':a[2],'b':b[1]}])
def test_paramType(param):
    a=param['a']
    b=param['b']
    re=requestApi().module(param)
    assert re['code']==21,'返回错误码不正确'
    assert re['message']=='empty or wrong params','返回message不正确'
    assert re['reference']==f'a={a},b={b}','返回reference不正确'

if __name__=='__main__':
    pytest.main(["-sv","test_paramType.py"])