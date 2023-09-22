from django.contrib import admin
from .models import *



@admin.register(Buyurtma)
class BuyurtmaAdmin(admin.ModelAdmin):
    list_display = ('client', 'mahsulot', 'sotuvchi', 'summa', 'miqdor','tolangan_summa','sana','nasiya')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['ism','fam','manzil','tel','umumiy_summa']


@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ["nom","kelgan_sana","miqdor","narx"]
# admin.site.register(Mahsulot)
# admin.site.register(Client)
admin.site.register(Sotuvchi)
# admin.site.register(Buyurtma)


# Register your models here.
