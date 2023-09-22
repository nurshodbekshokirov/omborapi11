from rest_framework import serializers
from .models import *

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


