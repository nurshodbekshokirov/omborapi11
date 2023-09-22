# Generated by Django 4.2.5 on 2023-09-13 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='tolangan_summa',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.client')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('sotuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.sotuvchi')),
            ],
        ),
    ]