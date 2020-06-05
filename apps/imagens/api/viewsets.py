from apps.imagens.models import Imagens
from rest_framework import viewsets
from .serializers import ImagensSerializer


class ImagensViewSet(viewsets.ModelViewSet):
    serializer_class = ImagensSerializer