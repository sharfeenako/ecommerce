# Generated by Django 4.2.6 on 2023-10-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_productimage_category_product_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
