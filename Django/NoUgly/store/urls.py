from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'product_kinds', ProductKindViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart_products', CartProuductViewSet)
router.register(r'product_random', ProductRandomViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = router.urls
