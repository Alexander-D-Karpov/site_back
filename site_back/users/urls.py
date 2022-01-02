from django.urls import path

from site_back.users.api.views import UserListApi


urlpatterns = [
    path('', UserListApi.as_view(), name='list')
]
