# Generated by Django 4.1.7 on 2023-03-02 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_orderedproduct_orderedproductmodel_and_more'),
        ('products', '0002_rename_product_productmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductModel',
            new_name='Product',
        ),
    ]
