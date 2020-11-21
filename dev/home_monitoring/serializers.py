from rest_framework import serializers
from home_monitoring.models import IOT
from django.utils import timezone


class IoTSerializer(serializers.Serializer):

    datatype = serializers.CharField(required=False, allow_blank=True, max_length=20)
    quantity = serializers.IntegerField(default=0)
    user_name = serializers.CharField(max_length=50)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        return IOT.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """

    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance