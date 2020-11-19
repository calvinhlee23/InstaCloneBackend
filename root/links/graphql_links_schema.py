from .graphql_links_create_mutation import CreateLink
from .graphql_links_types import LinkNode
from .models import Link
from django.db.models import Q
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

import graphene

# Query is used only for django
# class Query(graphene.ObjectType):
    # links = graphene.List(LinkNode, search=graphene.String())
    # def resolve_links(self, info, search=None, ** kwargs):
    #     if search:
    #         filter = (
    #             Q(url__icontains=search) |
    #             Q(description__icontains=search)
    #         )
    #         return Link.objects.filter(filter)
            
    #     return Link.objects.all()

class RelayQuery(graphene.ObjectType): 
    link = graphene.relay.Node.Field(LinkNode)
    links = DjangoFilterConnectionField(LinkNode)

class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
