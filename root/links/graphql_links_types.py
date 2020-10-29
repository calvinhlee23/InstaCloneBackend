from .models import Link
from graphene_django import DjangoObjectType

class LinkType(DjangoObjectType):
    class Meta:
        model = Link
