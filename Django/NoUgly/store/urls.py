from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_nam = 'store'

router = DefaultRouter()

router.register(r'product_kinds', ProductKindViewSet)
router.register(r'product', ProductViewSet)
router.register(r'product/<int:pk>/', ProductDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('products/', ProductList.as_view(), name='productCreate')
]
