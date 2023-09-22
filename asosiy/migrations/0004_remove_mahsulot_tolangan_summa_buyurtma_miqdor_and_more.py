# Generated by Django 4.2.5 on 2023-09-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0003_buyurtma_summa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahsulot',
            name='tolangan_summa',
        ),
        migrations.AddField(
            model_name='buyurtma',
            name='miqdor',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='buyurtma',
            name='nasiya',
            field=models.IntegerField(null=True, verbose_name='qarzi'),
        ),
        migrations.AddField(
            model_name='buyurtma',
            name='tolangan_summa',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='buyurtma',
            name='sana',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='umumiy_summa',
            field=models.PositiveIntegerField(default=0, verbose_name='qarz'),
        ),
    ]