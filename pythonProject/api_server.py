
import flask, json
from flask import request

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
module接口，需要传url、a、b
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)

# @server.route()可以将普通函数转变为服务 module接口的路径、请求方式
@server.route('/module', methods=['GET'])
def module():
    # 获取json请求格式的数据，因url请求参数只能为string类型
    #get_json 这个函数默认情况下只对 mime 为 application/json 的请求可以正确解析
    #1、header中添加content-type  2、force=True
    param=request.get_json(force=True)
    param_a = param.get('a')
    param_b = param.get('b')
    # 判断参数a、b是否为空，以及参数类型是否正确（a非必填的int型，b必填的string类型）
    if param_a!=None and param_b!=None:
        if isinstance(param_a,int) and isinstance(param_b,str):
            if param_a>0:
                res = {'code': 0, 'message': 'success','reference':f"a={param_a},b={param_b}"}
                return json.dumps(res, ensure_ascii=False)  # 将字典转换为json串, json是字符串
            else:
                res = {'code': 21, 'message': 'empty or wrong params','reference':f"a={param_a},b={param_b}"}
                return json.dumps(res, ensure_ascii=False)
        else:
            res = {'code': 21, 'message': 'empty or wrong params','reference':f"a={param_a},b={param_b}"}
            return json.dumps(res, ensure_ascii=False)
    elif param_a==None and param_b:
        if isinstance(param_b,str):
            res = {'code': 0, 'message': 'success','reference':f"a={param_a},b={param_b}"}
            return json.dumps(res, ensure_ascii=False)
        else:
            res = {'code': 21, 'message': 'empty or wrong params','reference':f"a={param_a},b={param_b}"}
            return json.dumps(res, ensure_ascii=False)
    elif param_b==None:
        res = {'code': 21, 'message': 'empty or wrong params','reference':f"a={param_a},b={param_b}"}
        return json.dumps(res, ensure_ascii=False)

if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
