from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        interfaces = graphene.relay.Node,
        filter_fields = {}
