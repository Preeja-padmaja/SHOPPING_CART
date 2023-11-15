from. import views
from django .urls import path
app_name='Shopping_Cart_App'
urlpatterns = [
    path('', views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.prodetails,name='procatdetails')
]