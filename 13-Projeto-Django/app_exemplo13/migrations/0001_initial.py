# Generated by Django 4.2.3 on 2023-08-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItensProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.CharField(max_length=25)),
                ('tipo', models.CharField(choices=[('I1', 'Inter'), ('I2', 'Inter 2'), ('I3', 'Inter 3')], max_length=2)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='Produtos/%Y/%m/%d')),
            ],
        ),
    ]
