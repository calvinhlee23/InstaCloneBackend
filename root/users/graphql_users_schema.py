from users.graphql_users_create_mutation import CreateUser
from django.contrib.auth import get_user_model
from .graphql_users_type import UserType
import graphene

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    def resolve_users(self, info):
        return get_user_model().objects.all()

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
