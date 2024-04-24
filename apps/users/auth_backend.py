# Third Party Stuff
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from apps.users.models import User

UserModel = get_user_model()


class UserAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticates a user based on the provided username and password.

        Args:
            request (HttpRequest): The HTTP request object.
            username (str, optional): The username of the user. Defaults to None.
            password (str, optional): The password of the user. Defaults to None.
            **kwargs: Additional keyword arguments.

        Returns:
            User"""
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = User.objects.get(
                email=username,
            )
            user = user
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
