# Generated by Django 4.0.2 on 2022-02-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('cel', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('stock_min', models.IntegerField()),
                ('stock_max', models.IntegerField()),
            ],
        ),
    ]