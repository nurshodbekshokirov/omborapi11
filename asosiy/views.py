from django.shortcuts import render
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login,logout


class MahsulotViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializers

    def create(self, request, *args, **kwargs):
        nom = request.data.get('nom')
        hajmi = request.data.get('hajmi')
        miqdor = request.data.get('miqdor')

        # Mahsulotni nom va hajmi bo'yicha bazada qidirish
        existing_mahsulot = Mahsulot.objects.filter(nom=nom, hajmi=hajmi).first()

        if existing_mahsulot:
            # Agar mavjud bo'lsa, yangi miqdorni qo'shib qo'yamiz
            existing_mahsulot.miqdor += int(miqdor)
            existing_mahsulot.narx
            existing_mahsulot.save()
            serializer = MahsulotSerializers(existing_mahsulot)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Agar mavjud emas bo'lsa, yangi mahsulotni yaratamiz
            serializer = MahsulotSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Sotuvchi.objects.all()
    serializer_class = SotuvchiSerializers

class RegisterAPIVIEW(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            validated_data = serializer.data
            validated_data['id']=user.id
            return Response(validated_data, status=status.HTTP_201_CREATED)

class LoginApiview(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
            )
            if user:
                login(request, user)
                return Response({"xabar":"Tizimga kiritildi"},status=status.HTTP_200_OK)
            return Response({"xabar":"Tizimga kiritilmadi"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class LogoutApiview(APIView):
    def get(self,request):
        logout(request)
        return Response({"xabar":"Tizimdan chiqarildi"})


class BuyurtmaViewset(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers



    # @action(detail=True, methods=["POST"])
    # def buyurtma(self, request, pk):
    #     if request.method == "POST":
    #         buyurtma =request.data




