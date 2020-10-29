import graphene
import links.graphql_links_schema as graphql_links_schema

class Query(graphql_links_schema.Query, graphene.ObjectType):
    pass

class Mutation(graphql_links_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,  mutation=Mutation)
