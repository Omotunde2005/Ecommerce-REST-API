# Generated by Django 4.2.2 on 2024-05-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0003_rename_cover_image_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='URL',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
