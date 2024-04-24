from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.auth.serializers import LoginSerializer
from apps.users import services as user_services
from apps.base import response
from apps.users.serializers import RegisterResponseSerializer, RegisterBaseSerializer

from apps.base.mixins import MultipleSerializerMixin

class AuthViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_classes = {
        "login": LoginSerializer,
        "register": RegisterBaseSerializer,
    }

    @action(methods=['POST'], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_services.get_and_authenticate_user(serializer.validated_data['email'], serializer.validated_data['password'])
        token = RefreshToken.for_user(user)
        user_response = RegisterResponseSerializer(user).data
        user_response["tokens"] = {
                "access": str(token.access_token),
                "refresh":str(token)
            }
        return response.Ok(user_response)

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_services.create_user_account(**serializer.validated_data)
        token = RefreshToken.for_user(user)
        user_response = RegisterResponseSerializer(user).data
        user_response["tokens"] = {
                "access": str(token.access_token),
                "refresh":str(token)
            }
        return response.Created(user_response) 








