from .graphql_vote_create_mutation import CreateVote
from .graphql_vote_types import VoteNode
from .models import Vote
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from links.graphql_links_schema import CreateLink

# class Query(ObjectType):
#     votes = List(VoteNode)
#     def resolve_votes(self, info, **kwargs):
#         return Vote.objects.all()
        
class RelayQuery(ObjectType):
    vote = relay.Node.Field(VoteNode)
    votes = DjangoFilterConnectionField(VoteNode)

class Mutation(ObjectType):
    create_vote = CreateVote.Field()
