# Generated by Django 4.1.7 on 2023-03-14 04:47

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import products.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=products.models.set_slugify)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='слаг')),
                ('description', models.TextField(max_length=20000, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/%Y-%m-%d', verbose_name='Картинки продукта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.productcategorymodel')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
