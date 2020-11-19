from links.models import Link
from links.graphql_links_schema import CreateLink
from .models import Vote
from users.graphql_users_types import UserNode
from links.graphql_links_types import LinkNode
import graphene


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserNode)
    link = graphene.Field(LinkNode)

    class Arguments:
        link_id = graphene.Int()

    def mutate(self, info, link_id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('User must be logged to vote!')

        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Link was not found given link_id')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)
