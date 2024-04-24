from django.shortcuts import render
from rest_framework import viewsets
from apps.friend_list.serializers import (
    FriendRequestActionSerializer, 
    FriendRequestBaseSerializer, 
    FriendRequestSerializer
)
from apps.friend_list.models import FriendRequest
from rest_framework import mixins
from rest_framework.decorators import action
from apps.base import response
from apps.base.exceptions import BadRequest
from apps.base.mixins import MultipleSerializerMixin
from apps.friend_list.filters import FriendListFilter


class FriendListApiViewSet(
    MultipleSerializerMixin, 
    mixins.ListModelMixin, 
    viewsets.GenericViewSet): 

    serializer_classes = {
        "send_request": FriendRequestBaseSerializer,
        "list_request": FriendRequestSerializer,
        "friend_request_action": FriendRequestActionSerializer
    }
    filter_backends = [FriendListFilter]

    def get_queryset(self):
        return FriendRequest.objects.filter(deleted_at__isnull=True)
    
    @action(methods=["POST"], detail=False, url_path="send_request")
    def send_request(self, request, *args, **kwargs):
        """
        Sends a friend request to the user specified in the request data.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The HTTP response containing the serialized friend request data.
        """
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        friend_request = serializer.save(sent_from=request.user)
        response_data = FriendRequestSerializer(friend_request).data
        return response.Ok(response_data)
    
    @action(methods=["POST"], detail=True, url_path="request_action")
    def friend_request_action(self, request, *args, **kwargs):
        """
        Handles the action of accepting or declining a friend request.

        Parameters:
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            response.Ok: The HTTP response containing the success message.

        Raises:
            BadRequest: If the friend request does not exist.
        """
        friend_request_obj = self.get_queryset()\
            .select_related("sent_to")\
                .filter(pk=kwargs.get('pk'), sent_to=request.user).first()
        if not friend_request_obj:
            raise BadRequest("no such friend-request")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_action = 2 if serializer.validated_data["action"] == "accept" else 3
        friend_request_obj.status = user_action
        friend_request_obj.save()
        response_data = "friend-request action successful"
        return response.Ok(response_data)

    @action(methods=["GET"], detail=False)
    def list_request(self, request, *args, **kwargs):
        """
        Retrieves and paginates a list of friend request objects based on the request data.

        Parameters:
            self: The instance of the class.
            request (HttpRequest): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: The paginated HTTP response containing friend request data.
        """
        request_objs = self.paginate_queryset(
            self.filter_queryset(self.get_queryset()\
                .select_related("sent_to").\
                    filter(sent_to=request.user)))
        if not request_objs:
            raise BadRequest("something went wrong with friend-requests") 
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(request_objs, many=True)
        return self.get_paginated_response(serializer.data)






