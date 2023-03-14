from autoslug import AutoSlugField
from django.db import models
import uuid
from slugify import slugify


def set_slugify(value) -> str:
    return slugify(value).replace(' ', '-')


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = AutoSlugField(populate_from='name', slugify=set_slugify, verbose_name='slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Наименование', max_length=1000)
    slug = AutoSlugField(populate_from='name', slugify=set_slugify, verbose_name='slug')
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(verbose_name='Описание', max_length=20000)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    count = models.IntegerField(verbose_name='Количество', )
    image = models.ImageField(upload_to='product_images/%Y-%m-%d', blank=True, null=True,
                              verbose_name='Картинки продукта')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name