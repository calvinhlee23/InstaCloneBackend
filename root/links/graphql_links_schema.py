from .graphql_links_create_mutation import CreateLink
from .graphql_links_types import LinkType
from .models import Link
from django.db.models import Q

import graphene

class Query(graphene.ObjectType):
    links = graphene.List(LinkType, search=graphene.String())

    def resolve_links(self, info, search=None, ** kwargs):
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(description__icontains=search)
            )
            return Link.objects.filter(filter)
            
        return Link.objects.all()

class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
