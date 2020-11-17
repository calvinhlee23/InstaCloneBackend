from .models import Vote
from graphene_django import DjangoObjectType

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote
