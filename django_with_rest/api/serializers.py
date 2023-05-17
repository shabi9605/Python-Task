
from rest_framework import serializers


class QuadraticSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()
    c = serializers.IntegerField()
