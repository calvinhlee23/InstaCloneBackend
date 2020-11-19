from .models import Vote
from graphene_django import DjangoObjectType
import graphene

class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = graphene.relay.Node,
        fields=['link']
        filter_fields = {}
