from django.db import models
from django.db.models.deletion import CASCADE
from authe.models import Author

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='категории', blank=False)

    class Meta:
        verbose_name = 'категоория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f"{self.name}"



class Size(models.Model):
    name = models.CharField(max_length=10, verbose_name='размер', blank=False)

    class Meta:
        verbose_name = 'размер'
        verbose_name_plural = 'размеры'

    def __str__(self):
        return f"{self.name}"

class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name='цвет', blank=False)

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'

    def __str__(self):
        return f"{self.name}"



class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='одежда')
    description = models.TextField(max_length=1000, verbose_name='описание')
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='категории')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='цена')
    color = models.ManyToManyField(Color, verbose_name='цвет')
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images', blank=True)
    size = models.ManyToManyField(Size, verbose_name='размеры')

    class Meta:
        verbose_name_plural = 'одежда'

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'), 
        ('progress', 'Progress'),
        ('finished', 'Finished'),
        ('canceled', 'Canceled') 
    ) 
    owner = models.ForeignKey(Author, on_delete=CASCADE, related_name='владелец')
    email = models.EmailField(unique=True, verbose_name='Почта')
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    def __str__(self):
        return f"{self.owner}"

class CartProduct(models.Model):
    product = models.ForeignKey(Product, related_name='cart_product', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cart_product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        verbose_name = 'одежда в корзине'
        verbose_name_plural = 'одежда в корзине'

    def __str__(self):
        return f"{self.product_name}"

    

