from .models import Link
from graphene_django import DjangoObjectType
from users.schema import UserType
import graphene

class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, description, url, user):
        link = Link(description=description, posted_by=user, url=url)
        link.save()
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=graphene.Field(UserType)
        )
