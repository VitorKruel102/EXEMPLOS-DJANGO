# Generated by Django 4.2.3 on 2023-08-18 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_exemplo18', '0002_alter_produtos_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produtos',
            options={'verbose_name_plural': 'Produto'},
        ),
        migrations.AlterModelTable(
            name='produtos',
            table=None,
        ),
    ]
