import django_filters

from site_back.users.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_admin')
