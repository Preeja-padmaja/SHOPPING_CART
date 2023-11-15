from django.db import models
from django.urls import reverse


# Create your models here.
class category_table(models.Model):
    c_name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('c_name',)
        verbose_name='category'
        verbose_name_plural='ctegories'
    def get_url(self):
        return reverse('Shopping_Cart_App:products_by_category',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.c_name)

class product_table(models.Model):
    p_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(category_table,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def get_url(self):
        return reverse('Shopping_Cart_App:procatdetails',args=[self.category.slug,self.slug])
    class Meta:
        ordering=('p_name',)
        verbose_name='product'
        verbose_name_plural='products'
    def __str__(self):
        return '{}'.format(self.p_name)



