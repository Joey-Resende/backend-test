from rest_framework import serializers
from core import models


class InvestAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invest
        fields = '__all__'
