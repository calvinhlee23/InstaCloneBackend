from .models import Link
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType

class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        interfaces = relay.Node,
        fields = ['url', 'description', ]
        filter_fields = {
            'description': ['exact', 'icontains', 'istartswith'],
        }

