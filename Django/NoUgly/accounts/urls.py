from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'destination', DestinationViewSet)


urlpatterns = router.urls
