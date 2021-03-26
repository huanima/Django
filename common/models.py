from django.db import models
# datetime用于O
import datetime



# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)

    phoneNumber = models.CharField(max_length=200)

    address = models.CharField(max_length=200)



class Medicine(models.Model):
    name = models.CharField(max_length=200)
    # 编号
    sn = models.CharField(max_length=200)
    # 描述
    desc = models.CharField(max_length=200)



# 一对多（客户和订单）
# 多对多（订单和药品）
class Order(models.Model):
    # 订单名
    name = models.CharField(max_length=200,null=True,blank=True)
    # 创建日期
    create_date = models.DateTimeField(default=datetime.datetime.now)
    # 一对一，客户
    # ForeignKey
    # on_delete:当这歌客户信息被删除时怎么办。
    # PROTECT:只有当这个customer对应的所有Order都被删除时，才可以删除这个customer
    # SET_NULL:删除这个客户信息后,Order里 customer = null（也就要设置Order的customer的null=True
    # CASCADE:如果客户信息被删除，删除所有链接的类的对应部分
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    # 多对多，药品
    # 不会显示在数据库表格中！
    medicines = models.ManyToManyField(Medicine,through='OrderMedicine')

# 继续多对多
class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine,on_delete=models.PROTECT)
    #每个药品数量
    amount = models.PositiveIntegerField()





# 一对一（客户和客户地址）
class ContactAddress(models.Model):
    # OneToOneField  一对一
    customer = models.OneToOneField(Customer,on_delete=models.PROTECT)
    homeAddress = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)





# 关于ORM

# 国家表
class Country(models.Model):
    name = models.CharField(max_length=200)

# 学生表，country是国家表的外键，形成一对多关系
class student(models.Model):
    name = models.CharField(max_length=200)
    grade = models.PositiveSmallIntegerField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT)














