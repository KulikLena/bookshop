from django.db import models
from django.contrib.auth import get_user_model
from forecast import models as fc_models

User = get_user_model()

class Cart (models.Model):
    customer = models.ForeignKey(
        User, 
        on_delete = models.PROTECT,
        related_name = "cart",
        verbose_name = 'customer',
        null = True,
        blank = True
    )
    created_date = models.DateTimeField (
        verbose_name = 'created',
        auto_created = True,
        auto_now = False 
    )
    updated_date = models.DateTimeField (
        verbose_name = 'updated',
        auto_created = True,
        auto_now = False 
    )

class BookInCart(models.Model):
    cart = models.ForeignKey (
        'order.Cart', 
        on_delete = models.PROTECT,
        related_name = "goods",
        verbose_name = 'Book in a Cart',
    )
    book = models.ForeignKey (
        fc_models.Book,
        on_delete = models.PROTECT,
        related_name = "goods",
        verbose_name = 'Book',
    )
    quantity = models.models.SmallIntegerField(
        verbose_name = 'Quantity'
        )
    price = models.DecimalField(
        verbose_name = "Price",
        decimal_places = 2,
        max_digits = 5,
        null = True,
        blank = True
    )
    created_date = models.DateTimeField (
        verbose_name = 'created',
        auto_created = True,
        auto_now = False 
    )
    updated_date = models.DateTimeField (
        verbose_name = 'updated',
        auto_created = True,
        auto_now = False 
    )
    
