
from rest_framework import serializers


class QuadraticSerializer(serializers.Serializer):
    a = serializers.FloatField()
    b = serializers.FloatField()
    c = serializers.FloatField()

    def validate(self, attrs):
        if attrs.get("a") == 0:
            raise serializers.ValidationError("The value of a not equal to zero")

        return super().validate(attrs)
