from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ['image']


class ProductKindSerializer(serializers.ModelSerializer):
    Product_kind.products = ProductSerializer(many=True)

    class Meta:
        model = Product_kind
        fields = ['id', 'kind']
