import graphene
import graphql_jwt
import links.graphql_links_schema as graphql_links_schema
import users.graphql_users_schema as graphql_users_schema
import vote.graphql_vote_schema as graphql_vote_schema

queries = [graphql_links_schema.RelayQuery,
           graphql_users_schema.Query, graphql_vote_schema.RelayQuery]
mutations = [graphql_links_schema.Mutation,
             graphql_users_schema.Mutation, graphql_vote_schema.Mutation]

class Query(*queries, graphene.ObjectType):
    pass

class Mutation(*mutations, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query,  mutation=Mutation)
