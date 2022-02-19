from __future__ import barry_as_FLUFL
from math import prod
from .serializers import *
from rest_framework import permissions, viewsets, status
from accounts.permissions import IsUserOrReadOnly
from .pagination import CartProuductNumberPagination, ProductPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter


class ProductKindViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product_kind.objects.all()
    serializer_class = ProductKindSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = ['name']
    filterset_fields = ['kind']
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    # http_method_names = ['post', 'get', 'put', 'delete']


class ProductRandomViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_queryset(self):
        pr = []
        count = 0
        while True:
            if count == 4:
                break
            num = Product.get_random3()
            if num not in pr:
                pr.append(num)
                count += 1
        return pr

    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]


class CartProuductViewSet(viewsets.ModelViewSet):
    queryset = Cart_product.objects.all()
    serializer_class = CartProuductSerializer
    pagination_class = CartProuductNumberPagination

    permission_classes = [
        permissions.IsAuthenticated, IsUserOrReadOnly]

    # 장바구니 전체삭제 구현

    @action(detail=False, methods=['DELETE'])
    def allDelete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            queryset = self.get_queryset().delete()
        return Response(queryset)

    def get_queryset(self):
        user = self.request.user
        queryset = Cart_product.objects.filter(uIDX=user)

        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    permission_classes = [
        permissions.IsAuthenticated, IsUserOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(uIDX=user)

        return queryset
