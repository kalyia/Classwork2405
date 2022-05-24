from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(primary_key=True, max_length=150, verbose_name='Category')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название товара')
    desc = models.TextField(max_length=500, verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Стоимость')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='product', verbose_name='Категория')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title