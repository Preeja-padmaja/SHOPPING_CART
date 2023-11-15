from django.contrib import admin

from Shopping_Cart_App.models import category_table, product_table

# Register your models here.
class category_admin(admin.ModelAdmin):
    list_display = ['c_name','slug']
    prepopulated_fields ={'slug':('c_name',)}

admin.site.register(category_table,category_admin)

class product_admin(admin.ModelAdmin):
    list_display = ['p_name','slug' ,'price','stock','category','available','created','updated']
    prepopulated_fields = {'slug': ('p_name',)}
    list_editable = ['price','stock','available']
    list_per_page = 20

admin.site.register(product_table,product_admin)
