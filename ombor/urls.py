"""
URL configuration for ombor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from asosiy.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



schema_view = get_schema_view(
   openapi.Info(
      title="Ombor API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Nurshodbek SHokirov, <nurshodbekshokirov@gmail.com>"),

   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('clientlar',ClientViewset)
router.register("mahsulotlar",MahsulotViewset)
router.register("sotuvchilar",SotuvchiViewset)
router.register("buyurtmalar",BuyurtmaViewset)




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("register/", RegisterAPIVIEW.as_view()),
    path('login/', LoginApiview.as_view()),
    path('logout/', LogoutApiview.as_view()),
    path('token_ber/', TokenObtainPairView.as_view()),
    path('token_yangila/', TokenRefreshView.as_view()),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]
