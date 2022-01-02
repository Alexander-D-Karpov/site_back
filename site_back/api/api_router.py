from django.urls import path, include

urlpatterns = [
    path('auth/', include(('site_back.authentication.urls', 'authentication'))),
    path('users/', include(('site_back.users.urls', 'users'))),
]
