from django.db import models
from Shopping_Cart_App.models import product_table
# Create your models here.
class cart_table(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='cart_table'
        ordering=['date_added']
    def __str__(self):
        return self.cart_id

class cart_item_table(models.Model):
    product=models.ForeignKey(product_table,on_delete=models.CASCADE)
    cart=models.ForeignKey(cart_table,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='cart_item_table'
    def sub_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return self.product
