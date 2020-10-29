from .graphql_links_create_mutation import CreateLink
from .models import Link
from graphene_django import DjangoObjectType
import graphene

class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
