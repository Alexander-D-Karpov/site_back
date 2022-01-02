from django.urls import path, include

urlpatterns = [
    path('users/', include(('site_back.users.urls', 'users'))),\
]
