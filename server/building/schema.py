import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoConnectionField

from .models import House
from .models import Room


class HouseNode(DjangoObjectType):

    class Meta:
        model = House
        interfaces = (graphene.relay.Node,)


class RoomNode(DjangoObjectType):

    class Meta:
        model = Room
        interfaces = (graphene.relay.Node,)


class Query(graphene.AbstractType):
    house = graphene.relay.Node.Field(HouseNode)
    all_house = DjangoConnectionField(HouseNode)

    room = graphene.relay.Node.Field(RoomNode)
    all_room = DjangoConnectionField(RoomNode)
