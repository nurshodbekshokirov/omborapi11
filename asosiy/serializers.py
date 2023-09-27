from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class SotuvchiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sotuvchi
        fields = "__all__"

class MahsulotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class BuyurtmaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField()

