from .models import Vote
from graphene_django import DjangoObjectType
from graphene import relay

class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = relay.Node,
        fields=['link']
        filter_fields = {}
