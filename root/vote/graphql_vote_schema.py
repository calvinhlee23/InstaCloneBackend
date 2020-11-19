# from .models import Vote
from .graphql_vote_create_mutation import CreateVote
from .graphql_vote_types import VoteNode
from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField

# class Query(ObjectType):
#     votes = List(VoteNode)
#     def resolve_votes(self, info, **kwargs):
#         return Vote.objects.all()
        
class RelayQuery(ObjectType):
    vote = relay.Node.Field(VoteNode)
    votes = DjangoFilterConnectionField(VoteNode)

class Mutation(ObjectType):
    create_vote = CreateVote.Field()
