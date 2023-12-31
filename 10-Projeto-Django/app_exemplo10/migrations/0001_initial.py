# Generated by Django 4.2.3 on 2023-08-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeDados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.CharField(max_length=5)),
                ('item2', models.CharField(max_length=10)),
                ('item3', models.CharField(max_length=15)),
                ('imagem', models.ImageField(blank=True, default=None, upload_to='Hom/HomeDados/%Y/%m/%d')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_modificacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
