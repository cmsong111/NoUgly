from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions, viewsets

# Create your views here.


class ProductKindViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product_kind.objects.all()
    serializer_class = ProductKindSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, ]
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post', 'get', 'put', 'delete']



