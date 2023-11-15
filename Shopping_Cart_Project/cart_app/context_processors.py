from .models import cart_table,cart_item_table
from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=cart_table.objects.filter(cart_id=_cart_id(request))
            cart_items=cart_item_table.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except cart_table.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)

