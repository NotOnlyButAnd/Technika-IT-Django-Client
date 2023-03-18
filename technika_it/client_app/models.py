from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

class Image(models.Model):
    image_id = models.IntegerField(primary_key=True)
    url = models.URLField()
    alt = models.CharField(max_length=100)

    class Meta:
        ordering = ["-image_id"]
        verbose_name = "Картинка"

    def __str__(self):
        return str(self.image_id)

#Да, его не было на том скрине, который лежит у меня в Pyrus, я его нашел в документации
class Manufacture(models.Model): #Дал себе вольность убрать множественное число из названия класса
    manufacture_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)

    #Возможность сортировки по названию производителя звучит хорошо
    class Meta:
        ordering = ["-manufacturer_id"]
        verbose_name = "Производитель"

    def __str__(self):
        return str(self.manufacture_id) + str(self.title)


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=75)

    class Meta:
        ordering = ["-category_id"]
        verbose_name = "Категория"

    def __str__(self):
        return str(self.category_id) + str(self.title)


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    #Поставил SetNULL при удалении, т.к. не придумал, что может быть другое при удалении картинки
    main_image_id = models.ForeignKey(Image, on_delete=models.SET_NULL, verbose_name="Главная картинка",null=True)
    #Думал Default поставить при удалении, но в интернетах много страшных вещей про него T_T
    main_category_id = models.ForeignKey(Categories, on_delete=models.SET_NULL, verbose_name="Категория",null=True)
    manufacturer_id = models.ForeignKey(Manufacture, on_delete=models.SET_NULL, verbose_name="Производитель",null=True)
    title = models.CharField(max_length=75)
    #В description заказывали большие поля... воть....
    description = models.TextField()
    price  = models.IntegerField()
    number_of_available = models.IntegerField()

    class Meta:
        ordering = ["-price","-product_id","-number_of_available"]
        verbose_name = "Товар"

    def __str__(self):
        return str(self.title) + str(self.price)


class Images_products(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.SET_NULL, verbose_name="Главная картинка",null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, verbose_name="Товар",null=True)
    #Как я понял, в этой таблице требовалось создать общийк ключ, он создается с помощью GenericForeignKey
    #надеюсь, что это то что нужно =) Для него мы import`нули штуковину
    id_images_products = GenericForeignKey(
        'product_id',
        'image_id',
    )

    class Meta:
        ordering = ["-product_id"]

    def __str__(self):
        return str(self.product_id)

#Тут все аналогично с классом выше
class Categories_products(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.SET_NULL, verbose_name="Категория", null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, verbose_name="Товар", null=True)
    id_images_products = GenericForeignKey(
        'product_id',
        'category_id',
    )

    class Meta:
        ordering = ["-product_id","-category_id"]

    def __str__(self):
        return str(self.category_id) + str(self.product_id)
