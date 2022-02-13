from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductNamePriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'image']


class ProductKindSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product_kind
        fields = '__all__'


class CartProuductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart_product
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['fIDX'] = ProductNamePriceSerializer(
            instance.fIDX).data
        return response
