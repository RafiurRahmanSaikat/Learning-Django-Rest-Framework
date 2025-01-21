import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr="iexact")
    # price = django_filters.CharFilter(lookup_expr="lt")

    class Meta:
        model = Product
        # fields = ["name", "price"]
        fields = {
            "name": ["exact", "contains"],
            "price": ["exact", "lt", "gt", "range"],
        }
