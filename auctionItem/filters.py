from django.contrib.auth.models import User
from . models import Lot
import django_filters

class ProductFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Lot
        fields = ['base_price','category','seller','is_live']