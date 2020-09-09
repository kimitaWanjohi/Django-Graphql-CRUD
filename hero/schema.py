import graphene
from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload

from .models import Universe, Hero


class UniverseType(DjangoObjectType):
    class Meta:
        model = Universe


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


class HeroQuery(graphene.ObjectType):
    all_universes = graphene.List(UniverseType)
    all_heroes = graphene.List(HeroType)

    hero = graphene.Field(HeroType, id=graphene.Int(), name=graphene.String())
    universe = graphene.Field(UniverseType, id=graphene.Int(), name=graphene.String())

    def resolve_all_universes(self, info, **kwargs):
        return Universe.objects.all()

    def resolve_all_heroes(self, info, **kwargs):
        return Hero.objects.all()

    def resovle_universe(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Universe.objects.get(pk=id)

        if name is not None:
            return Universe.objects.get(name=name)

        else:
            raise Exception('provide id or name')

    def resovle_hero(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Hero.objects.get(pk=id)

        if name is not None:
            return Hero.objects.get(name=name)

        else:
            raise Exception('provide id or name')


class CreateHero(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int()
        universe_id = graphene.Int()
        name = graphene.String()
        image = Upload(required=True)

    hero = graphene.Field(HeroType)

    def mutate(self, info, user_id, universe_id, name, image):
        hero = Hero.objects.create(user_id=user_id, universe_id=universe_id, name=name, image=image)
        hero.save()
        return CreateHero(hero=hero)


class UpdateHero(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        universe_id = graphene.Int()
        name = graphene.String()
        image = Upload(required=True)

    hero = graphene.Field(HeroType)

    def mutate(self, info, id, universe_id, name, image):
        hero = Hero.objects.get(pk=id)
        hero.name = name
        hero.universe_id = universe_id
        hero.image = image
        hero.save()
        return UpdateHero(hero=hero)


class HeroMutation(graphene.ObjectType):
    create_hero = CreateHero.Field()
    update_hero = UpdateHero.Field()