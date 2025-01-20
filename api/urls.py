from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductListCreateAPIView.as_view()),
    # path("products/create/", views.ProductCreateAPIView.as_view()),
    path("products/<int:pk>", views.ProductDetailAPIView.as_view()),
    path("products/info", views.ProductInfoAPIView.as_view()),
    path("orders/", views.OrderListAPIView.as_view()),
]
