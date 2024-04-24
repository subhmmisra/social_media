#from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from apps.users.auth.apis import AuthViewSet
from apps.users.apis import UserViewset
from apps.friend_list.apis import FriendListApiViewSet

default_router = DefaultRouter(trailing_slash=False)


default_router.register("auth", AuthViewSet, basename="auth")
default_router.register("users", UserViewset, basename="users")
default_router.register("friendship", FriendListApiViewSet, basename="friend_list")

urlpatterns = default_router.urls