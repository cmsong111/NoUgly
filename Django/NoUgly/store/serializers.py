from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ['image']


class ProductKindSerializer(serializers.ModelSerializer):
    Product_kind.products = ProductSerializer(many=True)

    class Meta:
        model = Product_kind

        fields = ['id', 'kind']
