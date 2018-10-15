from App.ext import db



# Create your models here.
class Main(db.Model): #  必须继承自db.Model

    __tablename__ = 'movies'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(64),unique=True)
    trackid =  db.Column(db.String(64),unique=True)


class MainWheel(db.Main):
    __tablename__='axf_wheel'

class MainNav(db.Main):
    __tablename__ = 'axf_nav'


class MainMustBuy(db.Main):
    __tablename__ = 'axf_mustbuy'

class MainShop(db.Main):
    __tablename__ = 'axf_shop'

class MainShow(db.Main):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categoryid = db.Column(db.String(64),unique=True)
    brandname = db.Column(db.String(64),unique=True)

    img1 = db.Column(db.String(64),unique=True)
    childcid1 = db.Column(db.String(64),unique=True)
    productid1 =db.Column(db.String(64),unique=True)
    longname1 =db.Column(db.String(64),unique=True)
    price1 = db.Column(db.String(64),unique=True)
    marketprice1 = db.Column(db.String(64),unique=True)

    img2 = db.Column(db.String(64),unique=True)
    childcid2 = db.Column(db.String(64),unique=True)
    productid2 = db.Column(db.String(64),unique=True)
    longname2 = db.Column(db.String(64),unique=True)
    price2 = db.Column(db.String(64),unique=True)
    marketprice2 = db.Column(db.String(64),unique=True)

    img3 = db.Column(db.String(64),unique=True)
    childcid3 = db.Column(db.String(64),unique=True)
    productid3 = db.Column(db.String(64),unique=True)
    longname3 = db.Column(db.String(64),unique=True)
    price3 = db.Column(db.String(64),unique=True)
    marketprice3 = db.Column(db.String(64),unique=True)

    __tablename__ =  'axf_mainshow'

class MainFoodTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typeid = db.Column(db.String(64),unique=True)
    typename = db.Column(db.String(64),unique=True)
    childtypenames  = db.Column(db.String(200),unique=True)
    typesort = db.Column(db.String(64),unique=True)

    __tablename__= 'axf_foodtypes'
class MainGoods(db.Model):
    # 商品id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productid = db.Column(db.String(64),unique=True)
    # 商品图片
    productimg = db.Column(db.String(64),unique=True)
    # 商品名称
    productname = db.Column(db.String(64),unique=True)
    # 商品长名称
    productlongname = db.Column(db.String(200),unique=True)
    # 是否精选
    isxf = db.Column(db.Boolean,default=False )
    # 是否买一赠一
    pmdesc = db.Column(db.String(200),unique=True)
    # 规格
    specifics = db.Column(db.String(200),unique=True)
    # 价格
    price = db.Column(db.String(200),unique=True)
    # 超市价格
    marketprice = db.Column(db.String(200),unique=True)
    # 组id
    categoryid = db.Column(db.String(200),unique=True)
    # 子类组id
    childcid = db.Column(db.String(200),unique=True)
    # 子类组名称
    childcidname = db.Column(db.String(200),unique=True)
    # 详情页id
    dealerid = db.Column(db.String(200),unique=True)
    # 库存
    storenums = db.Column(db.Integer)
    # 销量
    productnum = db.Column(db.Integer)

    __name__="axf_goods"

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(250),unique=True)
    smallname = db.Column(db.String(200),unique=True)
    phone = db.Column(db.String(200),unique=True)
    address =db.Column(db.String(200),unique=True)
    icon = db.Column(db.LargeBinary(length=2048))
    __name__ = "App_usermodel"

class CartModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    c_num=db.Column(db.Integer)
    is_choosed=db.Column(db.Boolean,default=True )
    ordermodel=db.relationship('OrderModel',secondary='registrations',
                               backref=db.backref('orders'),lazy='dynamic')
    __name__ = "App_cartmodel"


class OrderModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    o_num=db.Column(db.String(250),unique=True)
    is_pay=db.Column(db.Integer)
    __name__ = "App_ordermodel"

registrations = db.Table('App_ordergoodsmodel',
    db.Column('orderid', db.Integer, db.ForeignKey('App_ordermodel.id')),
    db.Column('goodsid', db.Integer, db.ForeignKey('App_cartmodel.id')),
    goods_num = db.Column(db.Integer,default=1)
)



# class OrderGoodsModel(models.Model):
#     orderid=models.ForeignKey(OrderModel)
#     goodsid = models.ForeignKey(MainGoods)
#
#     goods_num = db.Column(db.Integer,default=1)