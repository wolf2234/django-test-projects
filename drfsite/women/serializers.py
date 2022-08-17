import io
from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *

# time = datetime.now().isoformat()


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = "__all__"
        #fields = ('title', 'content', 'cat')


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_create = validated_data.get("time_create", instance.time_create)
#         instance.time_update = validated_data.get("time_update", time)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance
#
#     def delete(self, instance):
#         return instance.delete()


# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
# def encode():
#     model = WomenModel('Canabis', 'Content Canabis')
#     model_sr = WomenSerializer(model)
#     print(model_sr)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Canabis","content":"Content canabis"}')
#     data = JSONParser().parse(stream)
#     print(data, type(data))
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data, type(serializer.validated_data))
#     print(serializer)