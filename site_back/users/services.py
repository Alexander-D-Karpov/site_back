from typing import Optional

from site_back.users.models import User


def user_create(*,
                username: str,
                email: str,
                is_active: bool = True,
                is_admin: bool = False,
                password: Optional[str] = None
                ) -> User:
    user = User.objects.create_user(
        username=username,
        email=email,
        is_active=is_active,
        is_admin=is_admin,
        password=password
    )

    return user
