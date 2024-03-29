from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

class Image(models.Model):
    image_id = models.IntegerField(primary_key=True)
    url = models.URLField()
    alt = models.CharField(max_length=100)

    class Meta:
        ordering = ["-image_id"]
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

    def __str__(self):
        return str(self.image_id)


class Manufacture(models.Model):
    manufacture_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)

    #Возможность сортировки по названию производителя
    class Meta:
        ordering = ["-manufacture_id"]
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return str(self.manufacture_id) + str(self.title)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=75)

    class Meta:
        ordering = ["-category_id"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return str(self.category_id) + str(self.title)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    main_image = models.ForeignKey(Image, on_delete=models.SET_NULL, verbose_name="Главная картинка",null=True)
    main_category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория",null=True)
    manufacturer = models.ForeignKey(Manufacture, on_delete=models.SET_NULL, verbose_name="Производитель",null=True)
    title = models.CharField(max_length=75)
    description = models.TextField()
    price  = models.IntegerField()
    number_of_available = models.IntegerField()

    class Meta:
        ordering = ["-price","-product_id","-number_of_available"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


    def __str__(self):
        return str(self.title) + str(self.price)


class Image_product(models.Model):
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, verbose_name="Главная картинка",null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name="Товар",null=True)
    # id_images_products = GenericForeignKey(
    #     'product_id',
    #     'image_id',
    # )

    class Meta:
        ordering = ["-product"]
        verbose_name = "Фотография товара"
        verbose_name_plural = "Фотографии товара"

    def __str__(self):
        return str(self.product)


class Category_product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name="Товар", null=True)
    # id_images_products = GenericForeignKey(
    #     'product_id',
    #     'category_id'
    # )

    class Meta:
        ordering = ["-product","-category"]
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товара"

    def __str__(self):
        return str(self.category) + str(self.product)