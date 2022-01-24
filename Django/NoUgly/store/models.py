from math import prod
from django.db import models

# Create your models here.

#농작물 종류
class product_kind(models.Model):
    kind = models.CharField(primary_key=True)

#어글리 농작물
#농장물의 종류가 삭제해도 상품정보가 사라지면 안됨
class product(models.Model):
    fIDX = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    kind = models.ForeignKey(product_kind.kind, on_delete=models.SET_NULL)
    grade = models.CharField(max_length=5)
    date = models.DateTimeField()
    weight = models.IntegerField()
    Field = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()

#주문정보
#계정 및 상품이 사라져도 주문정보는 사라지면 안됨
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    count = models.IntegerField()
    price = models.IntegerField()
    purchase_time = models.DateTimeField()
    #uIDX = models.ForeignKey(member.uIDX, on_delete=models.SET_NULL)
    fIDX = models.ForeignKey(product.fIDX, on_delete=models.SET_NULL)

#배송지
class destination(models.Model):
    key = models.AutoField(primary_key=True)
    zipcode = models.IntegerField()
    adress = models.CharField(max_length=500)
    #uIDX = models.ForeignKey(member.uIDX)

#장바구니
class cart_product(models.Model):
    #uIDX = models.ForeignKey(member.uIDX)
    fIDX = models.ForeignKey(product.fIDX, on_delete=models.CASCADE)
    name = models.ForeignKey(product.name, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()