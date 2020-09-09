import graphene
from graphql_auth.schema import MeQuery
from graphql_auth import mutations
from users.schema import Query as CustomUserQuery
from users.schema import Mutation as userMutation
from hero.schema import HeroQuery, HeroMutation


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Query(HeroQuery, CustomUserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(HeroMutation, AuthMutation, userMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(Query, mutation=Mutation)
