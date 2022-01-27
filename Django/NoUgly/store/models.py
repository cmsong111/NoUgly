from django.db import models
from django.conf import settings

# Create your models here.

# 농작물 종류


class Product_kind(models.Model):
    kind = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.kind

# 어글리 농작물
# 농장물의 종류가 삭제해도 상품정보가 사라지면 안됨


class Product(models.Model):
    fIDX = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    kind = models.ForeignKey(
        Product_kind, on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=5)
    date = models.DateTimeField()
    weight = models.IntegerField()
    field = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    count = models.IntegerField()
    price = models.IntegerField()
    purchase_time = models.DateTimeField()
    uIDX = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='회원', null=True)
    fIDX = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

# 배송지


class Destination(models.Model):
    key = models.AutoField(primary_key=True)
    zipcode = models.IntegerField()
    adress = models.CharField(max_length=500)
    uIDX = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='회원', null=True)

# 장바구니


class Cart_product(models.Model):
    fIDX = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    uIDX = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='회원', null=True)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
