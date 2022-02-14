from itertools import product
from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions, viewsets
from accounts.permissions import IsUserOrReadOnly
from .pagination import CartProuductNumberPagination, ProductPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ProductKindViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product_kind.objects.all()
    serializer_class = ProductKindSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPageNumberPagination
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['kind']
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    # http_method_names = ['post', 'get', 'put', 'delete']


class CartProuductViewSet(viewsets.ModelViewSet):
    queryset = Cart_product.objects.all()
    serializer_class = CartProuductSerializer
    pagination_class = CartProuductNumberPagination

    permission_classes = [
        permissions.IsAuthenticated, IsUserOrReadOnly]
