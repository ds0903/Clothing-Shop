
from django.contrib import admin
from django.urls import path
from shop_app import views

from shop_app.views import kids, man, review_list, woman, cart,checkout

urlpatterns = [

    path("admin/", admin.site.urls),
    path("", review_list, name="main_page"),
    path("main_page", review_list, name="main_page"),
    path("man", man, name="man"),
    path("woman", woman, name="woman"),
    path("kids", kids, name="kids"),
    path('cart', cart, name='cart'),
    path('save_order/', views.save_order, name='save_order'),
    path('checkout/', checkout, name='checkout'),
]
