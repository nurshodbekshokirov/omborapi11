from django.contrib.auth.models import User
from django.db import models


class Sotuvchi(models.Model):
    ism = models.CharField(max_length=60)
    fam = models.CharField(max_length=60)
    manzil = models.CharField(max_length=60)
    tel_nomer = models.CharField(max_length=20)
    rasm = models.FileField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.ism

class Mahsulot(models.Model):
    nom = models.CharField(max_length=40)
    kelgan_sana = models.DateField(auto_now_add=True)
    hajmi = models.CharField(max_length=50, choices=(("0,5 litr ", "0.5 litr"),
                                                     ("1 litr","1 litr",), ("1,5 litr", "1,5 litr"),("2 litr", "2 litr")),blank=True)
    miqdor = models.PositiveSmallIntegerField()
    olchov = models.CharField(max_length=20)
    narx = models.PositiveIntegerField()
    rasm = models.FileField(null=True, blank=True)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}, {self.hajmi}"

    # def save(self, *args, **kwargs):
    #     umumiy = str(self.nom) + str(self.hajmi)
    #     mahsulotlar = Mahsulot.objects.all()
    #     if umumiy in mahsulotlar:

class Client(models.Model):
    ism = models.CharField(max_length=40)
    fam = models.CharField(max_length=40)
    manzil = models.CharField(max_length=70, blank=True)
    tel = models.CharField(max_length=70)
    rasm = models.FileField(null=True, blank=True)
    umumiy_summa = models.PositiveIntegerField(default=0, verbose_name="qarz")




    def __str__(self):
        return f"{self.ism} {self.fam}"


class Buyurtma(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)
    miqdor = models.IntegerField(null=True)
    summa = models.PositiveIntegerField(default=0)

    tolangan_summa = models.IntegerField(null=True)
    nasiya = models.IntegerField(verbose_name="qarzi", null=True, default=0)
    sana = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        # if (self.miqdor) < int(self.mahsulot.miqdor):
        #     return f"Omborda hozir {self.mahsulot.nom} dan {self.mahsulot.miqdor} mavjud xolos"

        self.summa = int(self.miqdor) * int(self.mahsulot.narx)
        self.nasiya = int(self.summa) - int(self.tolangan_summa)

        super(Buyurtma, self).save(*args, **kwargs)

        self.mahsulot.miqdor = int(self.mahsulot.miqdor) - int(self.miqdor)
        self.mahsulot.save()

        self.client.umumiy_summa = int(self.client.umumiy_summa) + int(self.nasiya)
        self.client.save()

    def __str__(self):
        return f"{self.mahsulot} {self.client}"


