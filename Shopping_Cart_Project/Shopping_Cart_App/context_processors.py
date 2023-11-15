from Shopping_Cart_App.models import category_table


def menu_links(requests):
    links=category_table.objects.all()
    return dict(links=links)
