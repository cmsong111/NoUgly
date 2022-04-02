from rest_framework import viewsets, permissions
from accounts.permissions import IsUserOrReadOnly


from .models import Destination
from .serializers import DestinationSerializer
# Create your views here.


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()

    serializer_class = DestinationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly
    ]

    def get_queryset(self):
        user = self.request.user
        queryset = Destination.objects.filter(uIDX=user)

        return queryset
