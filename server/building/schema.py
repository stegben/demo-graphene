import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoConnectionField

from .models import House
from .models import Room


class HouseNode(DjangoObjectType):

    half_price = graphene.Float()

    class Meta:
        model = House
        interfaces = (graphene.relay.Node,)

    def resolve_half_price(self, *args, **kwargs):
        return self.price / 2


class RoomNode(DjangoObjectType):

    class Meta:
        model = Room
        interfaces = (graphene.relay.Node,)


class CreateHouse(graphene.relay.ClientIDMutation):
    house = graphene.Field(HouseNode)

    class Input:
        name = graphene.String()
        price = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):
        house = House.objects.create(
            name=args.get('name', 'some random name'),
            price=args.get('price', 1000000),
        )
        return CreateHouse(house=house)

class Query(graphene.AbstractType):
    house = graphene.relay.Node.Field(HouseNode)
    all_house = DjangoConnectionField(HouseNode)

    room = graphene.relay.Node.Field(RoomNode)
    all_room = DjangoConnectionField(RoomNode)


class Mutation(graphene.AbstractType):
    create_house = CreateHouse.Field()
