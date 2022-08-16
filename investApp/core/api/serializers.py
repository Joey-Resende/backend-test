from rest_framework import serializers
from core import models


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Core
        fields = '__all__'
