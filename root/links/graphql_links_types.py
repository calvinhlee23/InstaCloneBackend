from .models import Link
from graphene_django import DjangoObjectType
import django_filters
import graphene

class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        interfaces = graphene.relay.Node,
        fields = ['url', 'description', ]
        filter_fields = {
            'description': ['exact', 'icontains', 'istartswith'],
        }

