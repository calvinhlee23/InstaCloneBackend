from .graphql_vote_create_mutation import CreateVote
from .graphql_vote_types import VoteNode
from .models import Vote
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from links.graphql_links_schema import CreateLink
import graphene

# class Query(graphene.ObjectType):
#     votes = graphene.List(VoteNode)
#     def resolve_votes(self, info, **kwargs):
#         return Vote.objects.all()
        
class RelayQuery(graphene.ObjectType):
    vote = graphene.relay.Node.Field(VoteNode)
    votes = DjangoFilterConnectionField(VoteNode)

class Mutation(graphene.ObjectType):
    create_vote = CreateVote.Field()
