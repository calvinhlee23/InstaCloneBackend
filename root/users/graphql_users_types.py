from django.contrib.auth import get_user_model
from graphene import relay
from graphene_django import DjangoObjectType

class UserNode(DjangoObjectType):
    class Meta:
        filter_fields = {}
        interfaces = relay.Node,
        model = get_user_model()
