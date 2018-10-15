from App.ext import db

from django.db import models

# Create your models here.
class Main(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=32)
    trackid=models.CharField(max_length=20)
    class Meta:
        abstract=True

class MainWheel(Main):
    class Meta:
        db_table='axf_wheel'

class MainNav(Main):
    class Meta:
        db_table='axf_nav'


class MainMustBuy(Main):
    class Meta:
        db_table='axf_mustbuy'

class MainShop(Main):
    class Meta:
        db_table='axf_shop'

class MainShow(Main):
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'

class MainFoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=32)
    childtypenames  = models.CharField(max_length=200)
    typesort = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_foodtypes'
class MainGoods(models.Model):
    # 商品id
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=150)
    # 商品名称
    productname = models.CharField(max_length=50)
    # 商品长名称
    productlongname = models.CharField(max_length=100)
    # 是否精选
    isxf = models.NullBooleanField(default=False)
    # 是否买一赠一
    pmdesc = models.CharField(max_length=10)
    # 规格
    specifics = models.CharField(max_length=20)
    # 价格
    price = models.CharField(max_length=10)
    # 超市价格
    marketprice = models.CharField(max_length=10)
    # 组id
    categoryid = models.CharField(max_length=10)
    # 子类组id
    childcid = models.CharField(max_length=10)
    # 子类组名称
    childcidname = models.CharField(max_length=10)
    # 详情页id
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销量
    productnum = models.IntegerField()

    class Meta:
        db_table = "axf_goods"

class UserModel(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=256)


    smallname = models.CharField(max_length=32)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=256)
    icon = models.ImageField(upload_to='icons')

class CartModel(models.Model):
    goodsid=models.ForeignKey(MainGoods)
    userid=models.ForeignKey(UserModel)
    c_num=models.IntegerField(default=1)
    is_choosed=models.BooleanField(default=True)

class OrderModel(models.Model):
    userid=models.ForeignKey(UserModel)
    o_num=models.CharField(max_length=150)
    is_pay=models.IntegerField(default=0)


class OrderGoodsModel(models.Model):
    orderid=models.ForeignKey(OrderModel)
    goodsid = models.ForeignKey(MainGoods)

    goods_num = models.IntegerField(default=1)