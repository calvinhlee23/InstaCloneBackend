from .graphql_vote_create_mutation import CreateVote
from .graphql_vote_types import VoteType
from .models import Vote
from links.graphql_links_schema import CreateLink
import graphene

class Query(graphene.ObjectType):
    votes = graphene.List(VoteType)
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
        
class Mutation(graphene.ObjectType):
    create_vote = CreateVote.Field()
