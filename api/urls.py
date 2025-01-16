from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:pr>", views.product_details),
    path("orders/", views.order_list),
]
