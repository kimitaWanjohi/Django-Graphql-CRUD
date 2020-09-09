import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model
from graphene_file_upload.scalars import Upload

from .models import Profile



class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_ = graphene.Field(UserType, id=graphene.Int(), name=graphene.String())

    all_profiles = graphene.List(ProfileType)
    profile = graphene.Field(ProfileType, user_id=graphene.Int())

    def resolve_all_users(self, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_user_(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return get_user_model().objects.get(pk=id)
        if name is not None:
            return get_user_model().objects.all(username=name)
        else:
            raise Exception('username or id is required')


    def resolve_all_profiles(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_profile(self, info, **kwargs):
        user_id = kwargs.get('user_id')

        if user_id is not None:
            return Profile.objects.get(user_id=user_id)


class ProfileUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        f_name = graphene.String()
        l_name = graphene.String()
        image = Upload(required=True)

    profile = graphene.Field(ProfileType)
    success = False
    def mutate(self, info, id, f_name, l_name, image):
        profile = Profile.objects.get(pk=id)
        profile.first_name = f_name
        profile.last_name = l_name
        profile.user_image = image
        profile.save()
        return ProfileUpdate(profile=profile)
    success = True


class Mutation(graphene.ObjectType):
    profile_update = ProfileUpdate.Field()
