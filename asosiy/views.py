from django.shortcuts import render
from rest_framework.response import Response

from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


class MahsulotViewset(ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializers

    @action(detail=True, methods=["GET","POST"])
    def clientlar(self,request,pk):

        if request.method == "POST":
            client = request.data
            serializer = SotuvchiSerializers(data=client)
            if serializer.is_valid():
                serializer.save(mahsulot=self.get_object())
        mahsulot = self.get_object()
        clientlar = Client.objects.filter(buyurtma__mahsulot=mahsulot)
        serializer =  ClientSerializers(clientlar,many=True)
        return Response(serializer.data)








class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

    @action(detail=True, methods=["GET", "POST"])
    def mahsulotlar(self, request, pk):

        if request.method == "POST":
            mahsulot = request.data
            serializer = MahsulotSerializers(data=mahsulot)
            if serializer.is_valid():
                serializer.save(client=self.get_object())
        client = self.get_object()
        mahsulotlar = Mahsulot.objects.filter(buyurtma__client=client)

        serializer = MahsulotSerializers(mahsulotlar, many=True)
        return Response(serializer.data)

class SotuvchiViewset(ModelViewSet):
    queryset = Sotuvchi.objects.all()
    serializer_class = SotuvchiSerializers



class BuyurtmaViewset(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers



    @action(detail=True, methods=["POST"])
    def buyurtma(self, request, pk):
        if request.method == "POST":
            buyurtma =request.data




