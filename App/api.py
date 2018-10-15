from flask import request
from flask.json import jsonify
from flask_restful import Resource, fields, marshal_with, reqparse

# 类视图
from App.ext import db
from App.models import Cat


class HelloWorld(Resource):

    def get(self):

       return {"hello":"world"}



catone_fields={
    "catname":fields.String(attribute="c_name",),
    "catage":fields.Integer(attribute="c_age"),
}


cat_fields = {
    "msg": fields.String,
    "status":fields.String(default="201"),
    "url":fields.Url("zhoujiajia",absolute=True),
    "cat":fields.Nested(catone_fields),
}




# 参数解析   代替了咱们平常的`request.args.get()
# parse = reqparse.RequestParser()
# parse.add_argument("catname",type=str,help="这里没有名字")
# parse.add_argument("catage",type=str)


class CatResouce(Resource):

    @marshal_with(cat_fields)
    def get(self):

        # args = parse.parse_args()
        #
        # print(args)
        #
        # print(type(args))
        catname=request.args.get('catname')
        catage=request.args.get('catage')
        cats=Cat.query.filter(Cat.c_age<17).all()

        # catname = args.get("catname")



        return {"msg": "OK", "cat": cats}
    def post(self):
        catname=request.form.get('catname')
        catage=request.form.get('catage')
        cats=Cat.query.filter(Cat.c_name==catname).all()
        if len(cats)>0:
            return {'msg':'cat is exist','status':'409'}

        cat=Cat()
        cat.c_name=catname
        cat.c_age=catage
        db.session.add(cat)
        db.session.commit()
        return jsonify({'msg':'cat is create success','status':'201'})