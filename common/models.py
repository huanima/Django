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



# 如果要访问Order中的某个订单customer的名字（例如这个订单的叫Order1:
# Order1.customer.name
# 因为Order1.customer相当于Customer里的一个对象，.name就相当于 .属性





# 关于ORM

# 国家表
class Country(models.Model):
    name = models.CharField(max_length=200)

# 学生表，country是国家表的外键，形成一对多关系
class Student(models.Model):
    name = models.CharField(max_length=200)
    grade = models.PositiveSmallIntegerField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT)


# ？ 1.1.如果要访问Student中的某个学生的国家（例如这个学生是 s1:
# s1.country.name
# 因为s1.country相当于Country里的一个对象，.name就相当于 .属性

# ？ 1.2.搜索表中所以一年级的学生
# Student.objects.filter(grade=1).value()

# ？ 1.3.如果想筛选所有一年级中国的学生
# X错！       Student.objects.filter(grade=1，country='中国').value()
# 一般的方法：  cn = Country.objects.get(name='中国')
#            Student.objects.filter(grade=1,country_id=cn.id).value()
# √对！       Student.objects.filter(grade=1，country__name='中国').value()

# ？ 1.4.如果筛选筛选所有一年级中国的学生，并仅输出姓名和国家
# √对！ Student.objects.filter(grade=1，country__name='中国').value('name','country__name')

# ？ 1.5.country__name这种命名很不适合前后端交接，如果想要改名字可以：
# from django.db.models import F
# Student.objects.annotate(
#     countryname = F('country__name'),
#     studentname = F('name')
#     )\
#     .filter(grade=1,countryname='中国').value('studentname','countryname')


# ？ 2.1.反向，输出所有中国学生
# cn = Country.objects.get(name='中国')
# cn.student_set.all()
#     这样输出结果是对象！
#     [<Student>:Student object(1),<Student>:Student object(2)]
# 所以 cn.student_set.all()[0].name    就能输出 第一个对象的name

# ？ 2.2.定义反向关联名
# 在定义类的时候
# class Student(models.Model):
#     name = models.CharField(max_length=200)
#     grade = models.PositiveSmallIntegerField()
#     country = models.ForeignKey(Country, on_delete=models.PROTECT,related_name='students')
# 那么2.1.的问题可以如下
# cn = Country.objects.get(name='中国')
# cn.students.all()


# ？ 2.3.所有一年级学生 的国家名字
# 一般的方法：先找到所有一年级学生的国家id。values_list 以list输出，flat=True 不是键值对的输出，只输出值
#     country_ids = Student.objects.filter(grade=1).values_list('country',flat=True)
#     id__in=  在这个列表的id
#     Country.objects.filter(id__in=country_ids).value()
# √   链接到另一个表里就要表名全小写。distinct()去重，据说distinct()对MySQL数据库无效
#     Country.objects.filter(student__grade=1).value()distinct()
# 注：如果定义了反向关联名，用反向关联名啊
#     Country.objects.filter(students__grade=1).value()distinct()
