import graphene
import building.schema


class Query(building.schema.Query,
            graphene.ObjectType):
    test = graphene.String()

    def resolve_test(self, *args, **kwargs):
        return 'Hello World!'


class Mutation(building.schema.Mutation,
               graphene.ObjectType):
    test = graphene.String()

    def resolve_test(self, *args, **kwargs):
        return 'Hello World!'


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
