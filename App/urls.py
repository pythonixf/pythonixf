from flask_restful import Api

from App.api import HelloWorld, CatResouce

api = Api()

# api添加资源路径时,放到全局上
api.add_resource(HelloWorld, "/hello/")

api.add_resource(CatResouce,"/cat/",endpoint="zhoujiajia")

def init_url(app):
    api.init_app(app)


