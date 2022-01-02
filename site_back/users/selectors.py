from site_back.common.types import QuerySetType

from site_back.users.models import User
from site_back.users.filters import UserFilter


def user_get_login_data(*, user: User):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_active': user.is_active,
        'is_admin': user.is_admin,
        'is_superuser': user.is_superuser,
    }


def user_list(*, filters=None) -> QuerySetType[User]:
    filters = filters or {}

    users = User.objects.all()

    return UserFilter(filters, users).qs
