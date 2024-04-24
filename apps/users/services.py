# apps/users/services.py
# Third Party Stuff
from django.contrib.auth import get_user_model

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model


from apps.base import exceptions as exc
from apps.users.models import User


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise exc.WrongArguments("Invalid username/password. Please try again!")

    return user


def create_user_account(email, password=None, **kwargs):
    # TODO: Remove case conversions
    user_details = kwargs
    if password is not None:
        user_details["password"] = password
    user = get_user_model().objects.create_user(email=email, **user_details)
    return user


def get_user_by_email(email: str):
    user_email = User.objects.filter(email=email).first()
    user = user_email.user if user_email else None
    return user

