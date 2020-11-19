from .models import Vote
from graphene_django import DjangoObjectType
import graphene

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = graphene.relay.Node,
