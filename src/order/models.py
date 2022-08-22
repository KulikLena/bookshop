from django.db import models
from django.contrib.auth import get_user_model
from forecast import models as fc_models

User = get_user_model()
MORNING = '10am - 5pm'
EVENING ='5pm - 10pm'

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
        auto_now_add= True,
        auto_now = False, 
        null = True
    )
    updated_date = models.DateTimeField (
        verbose_name = 'updated',
        auto_now_add = True,
        auto_now = False, 
        null = True
    )
    def total_price(self):
        total = 0
        for good in self.goods.all():
            total += good.price
        return total


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
    quantity = models.SmallIntegerField(
        verbose_name = 'quantity'
        )
    price = models.DecimalField(
        verbose_name = "price",
        decimal_places = 2,
        max_digits = 15,
        null = True,
        blank = True
    )
    created_date = models.DateTimeField (
        verbose_name = 'created',
        auto_created = True,
        auto_now = False, 
        null = True
    )
    updated_date = models.DateTimeField (
        verbose_name = 'updated',
        auto_created = True,
        auto_now = False, 
        null = True
    )
    
class Order (models.Model):
    cart = models.ForeignKey (
        'order.Cart', 
        on_delete = models.PROTECT,
        related_name = "orders",
        verbose_name = 'Book in a Cart'    )
    name = models.CharField(max_length=150, null = False, default='John Doe')
    telephone = models.CharField(max_length=17, default='+375-00-000-00-00', null = False)
    address=models.CharField(max_length=140, null = False, default='somewhere' )
    #desired_delivery_time=models.CharField(max_length=140,
     #  choices=[(MORNING,'10am - 5pm'), (EVENING, '5pm - 10pm')],
      # blank=True)


    

