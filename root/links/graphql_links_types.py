from .models import Link
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
import django_filters

# class LinkNodeFilter(django_filters.FilterSet):
#     # Do case-insensitive lookups on 'name'
#     description = django_filters.CharFilter(lookup_expr=['icontains'])
#     class Meta:
#         model = Link
#         fields = ['description']

class LinkNode(DjangoObjectType):
    class Meta:
        fields = ['url', 'description']
        # filterset_class = LinkNodeFilter
        filter_fields = {
            'description': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = relay.Node,
        model = Link


        

