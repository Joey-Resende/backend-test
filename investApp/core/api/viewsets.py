from rest_framework import viewsets
from core.api import serializers
from core import models


class CoreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CoreSerializer
    queryset = models.Core.objects.all()
