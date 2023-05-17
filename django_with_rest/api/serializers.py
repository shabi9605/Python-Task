
from rest_framework import serializers


class QuadraticSerializer(serializers.Serializer):
    a = serializers.FloatField()
    b = serializers.FloatField()
    c = serializers.FloatField()
