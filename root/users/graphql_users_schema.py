from .graphql_users_types import UserType
from django.contrib.auth import get_user_model
from users.graphql_users_create_mutation import CreateUser
import graphene

class Query(graphene.ObjectType):
    current_user = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()
        
    def resolve_current_user(self, info): 
        user = info.context.user
        if user.is_anonymous:
                raise Exception('No Current User Found')
        return user

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
