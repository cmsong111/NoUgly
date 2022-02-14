from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'product_kinds', ProductKindViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart_products', CartProuductViewSet)

urlpatterns = router.urls
