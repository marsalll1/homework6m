from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .permissions import IsModerator
from common.validators import validate_age


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]

    def perform_create(self, serializer):
        validate_age(self.request)
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()
        return Product.objects.filter(owner=self.request.user)