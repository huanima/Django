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




class Order(models.Model):
    # 订单名
    name = models.CharField(max_length=200,null=True,blank=True)
    # 创建日期
    create_date = models.DateTimeField(default=datetime.datetime.now)
    # 客户
    # on_delete:当这歌客户信息被删除时怎么办。
    # PROTECT:只有当这个customer对应的所有Order都被删除时，才可以删除这个customer
    # SET_NULL:删除这个客户信息后,Order里 customer = null（也就要设置Order的customer的null=True
    # CASCADE:如果客户信息被删除，删除所有链接的类的对应部分
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
