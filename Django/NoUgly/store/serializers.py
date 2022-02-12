from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductKindSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product_kind
        fields = '__all__'


class CartProuductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_product
        field = '__all__'
