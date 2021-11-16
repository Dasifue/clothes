from django.db import models
from django.db.models.deletion import CASCADE

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='категории', blank=False)

    class Meta:
        verbose_name = 'категоория'
        verbose_name_plural = 'категории'

    def __init__(self):
        return f"{self.name}"



class Size(models.Model):
    name = models.CharField(max_length=10, verbose_name='размер', blank=False)

    class Meta:
        verbose_name = 'размер'
        verbose_name_plural = 'размеры'

    def __init__(self):
        return f"{self.name}"



class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='одежда')
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='категории')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='цена')
    count = models.ImageField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images', blank=True)
    size = models.ForeignKey(Size, on_delete=CASCADE, related_name='размер')

    class Meta:
        verbose_name_plural = 'одежда'

    def __init__(self):
        return f"{self.name}"


class Cart(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'), 
        ('progress', 'Progress'),
        ('finished', 'Finished'),
        ('canceled', 'Canceled') 
    ) 
    owner = models.CharField(max_length=30, verbose_name='владелец')
    number = models.CharField(max_length=20, verbose_name='номер владельца')
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    def __init__(self):
        return f"{self.owner}"

class CartProduct(models.Model):
    product = models.ForeignKey(Product, related_name='cart_product', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cart_product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __init__(self):
        return f"{self.product_name}"

    

