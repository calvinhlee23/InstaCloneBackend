from .models import Vote
from graphene_django import DjangoObjectType
from graphene import relay

class VoteNode(DjangoObjectType):
    class Meta:
        fields=['link']
        filter_fields = {}
        interfaces = relay.Node,
        model = Vote
