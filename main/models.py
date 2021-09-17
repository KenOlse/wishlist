from django.db import models

from users.models import AdvUser

class Product(models.Model):
    title = models.CharField('Продукт', max_length=50)
    link = models.URLField(
        'Інтернет-адреса', help_text='Укажіть інтернет адресу')
    price = models.IntegerField('Ціна продукту', help_text='Укажіть ціну')
    added = models.DateTimeField(
        'Додано', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'



class WishListUser(models.Model):
    title = models.CharField('Title', max_length=120)
    owner = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    product_user = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)

    def __str__(self):
        return self.title