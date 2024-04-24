# # middleware.py
import time
from django.http import HttpResponseForbidden
from django.utils import timezone


class FriendRequestLimitMiddleware:
    LIMIT = 3
    WINDOW = 60  # Seconds in a minute

    def __init__(self, get_response):
        self.get_response = get_response
        self.request_data = {}

    def __call__(self, request):
        """
        This function is the implementation of the __call__ method for the FriendRequestLimitMiddleware class.
        It is responsible for handling the incoming request and checking if it matches the specific endpoint '/api/v1/friendship/send_request'.
        If the request matches, it performs rate limiting by checking the number of requests made within a certain time window.
        If the number of requests exceeds the limit, it returns an HttpResponseForbidden object with the message 'Rate limit exceeded'.
        Otherwise, it appends the current timestamp to the list of requests made by the user.
        
        Parameters:
        - request: The incoming request object.
        
        Returns:
        - The response of the get_response method of the FriendRequestLimitMiddleware class.
        """
        if request.path == '/api/v1/friendship/send_request':  # Match the specific endpoint
            user_id = request.user.id
            now = timezone.now()

            if user_id in self.request_data:
                last_requests = self.request_data[user_id]
                if now - last_requests[0] < timezone.timedelta(seconds=self.WINDOW):
                    if len(last_requests) >= self.LIMIT:
                        return HttpResponseForbidden('Rate limit exceeded')
                else:
                    self.request_data[user_id] = []
            else:
                self.request_data[user_id] = []

            self.request_data[user_id].append(now)

        return self.get_response(request)
