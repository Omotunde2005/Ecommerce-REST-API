# Generated by Django 4.2.2 on 2024-05-06 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0005_sale_saleitem_sale_products_sale_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]