from django_filters import CharFilter, BooleanFilter, NumberFilter
from django_filters.rest_framework import FilterSet
from django.db.models import Count

from api.models import User


class UserFilter(FilterSet):
    def filter_distance(self, queryset, name, value):
        queryset = queryset.annotate(distance=Count('id'))

        return queryset

    first_name = CharFilter(field_name='first_name', lookup_expr='iexact')
    last_name = CharFilter(field_name='last_name', lookup_expr='iexact')
    gender = BooleanFilter(field_name='gender', lookup_expr='exact')
    distance = NumberFilter(method='filter_distance')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'distance']
