from .graphql_links_create_mutation import CreateLink
from .graphql_links_types import LinkType
from .models import Link
import graphene

class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
