from django.contrib import admin

from .models import Order, OrderItem, Product, User


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(User)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "stock"]


admin.site.register(Product, ProductAdmin)
