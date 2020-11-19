# from .models import Link
# from django.db.models import Q
from .graphql_links_create_mutation import CreateLink
from .graphql_links_types import LinkNode
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

# Query is used only for django
# class Query(ObjectType):
    # links = List(LinkNode, search=String())
    # def resolve_links(self, info, search=None, **kwargs):
    #     if search:
    #         filter = (
    #             Q(url__icontains=search) |
    #             Q(description__icontains=search)
    #         )
    #         return Link.objects.filter(filter)
    #     return Link.objects.all()

class RelayQuery(ObjectType): 
    link = relay.Node.Field(LinkNode)
    links = DjangoFilterConnectionField(LinkNode)

class Mutation(ObjectType):
    create_link = CreateLink.Field()
