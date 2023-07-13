from django_filters import CharFilter, BooleanFilter
from django_filters.rest_framework import FilterSet

from api.models import User


class UserFilter(FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='iexact')
    last_name = CharFilter(field_name='last_name', lookup_expr='iexact')
    gender = BooleanFilter(field_name='gender', lookup_expr='exact')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender']
