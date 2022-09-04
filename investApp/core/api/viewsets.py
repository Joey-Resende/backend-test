from rest_framework import viewsets
from core.api import serializers
from core import models


class InvestAppViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InvestAppSerializer
    queryset = models.Invest.objects.all()
