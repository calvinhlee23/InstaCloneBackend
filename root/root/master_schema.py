import graphene
import links.graphql_links_schema as graphql_links_schema
import users.graphql_users_schema as graphql_users_schema

queries = [graphql_links_schema.Query, graphql_users_schema.Query]
mutations = [graphql_links_schema.Mutation, graphql_users_schema.Mutation]

class Query(*queries, graphene.ObjectType):
    pass

class Mutation(*mutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,  mutation=Mutation)
