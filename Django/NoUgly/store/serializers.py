from .models import *
from rest_framework import serializers
from rest_framework import viewsets

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('fIDX', 'name', 'kind', 'grade', 'date', 'weight', 'field', 'price', 'image')
        

class ProductKindSerializer(serializers.ModelSerializer):
    Product_kind.kind = ProductSerializer(many=True ,read_only=True)

    class Meta:
        model = Product_kind
        fields = '__all__'