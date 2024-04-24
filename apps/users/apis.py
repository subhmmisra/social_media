from django.shortcuts import render
from rest_framework import viewsets
from apps.users.models import UserManager, User
from apps.users.serializers import (
    RegisterResponseSerializer
)
from rest_framework.decorators import action
from apps.base import response
from apps.base.mixins import MultipleSerializerMixin
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from apps.base.filters import SearchWithWhitespaceFilter


class UserViewset(MultipleSerializerMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_classes = {
        "list": RegisterResponseSerializer
    }
    filter_backends = [SearchWithWhitespaceFilter,]
    search_fields = ["first_name", "last_name", "email"]

    def get_queryset(self):
        return User.objects.all()

    def list(self, request, *args, **kwargs):
        """
        This function takes a request parameter and filters the queryset based on the request. 
        It then generates a paginated response using the paginated_response function and returns an Ok response with the data.
        """
        queryset = self.filter_queryset(queryset=self.get_queryset())
        user_objs = self.paginate_queryset(queryset)
        serializer = self.get_serializer_class()
        response_data = serializer(user_objs, many=True).data
        return self.get_paginated_response(response_data)


