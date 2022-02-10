from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'product_kinds', ProductKindViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('products/', ProductList.as_view(), name='productCreate')
]
