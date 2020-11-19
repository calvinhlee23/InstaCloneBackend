from .graphql_users_types import UserNode
from django.contrib.auth import get_user_model
from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField
from users.graphql_users_create_mutation import CreateUser

# class Query(ObjectType):
#     current_user = Field(UserType)
#     users = List(UserType)

#     def resolve_users(self, info):
#         return get_user_model().objects.all()
        
#     def resolve_current_user(self, info): 
#         user = info.context.user
#         if user.is_anonymous:
#                 raise Exception('No Current User Found')
#         return user

class RelayQuery(ObjectType): 
    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

class Mutation(ObjectType):
    create_user = CreateUser.Field()
