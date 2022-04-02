
import datetime
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

    # products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product_kind
        fields = '__all__'


class CartProuductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_product
        exclude = ['created_at', 'updated_at']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['fIDX'] = ProductNamePriceSerializer(
            instance.fIDX).data
        return response


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['uIDX']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['fIDX'] = ProductNamePriceSerializer(
            instance.fIDX).data
        return response
