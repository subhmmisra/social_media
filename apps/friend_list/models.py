from django.db import models
from apps.base.models import BaseModel
from apps.users.models import User

# Create your models here.


class FriendRequest(BaseModel):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Rejected'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    # store the user that has sent the request
    sent_from = models.ForeignKey(User, related_name="requests_sent", on_delete=models.CASCADE)
    # store the user that has received the request
    sent_to = models.ForeignKey(User, related_name="requests_received", on_delete=models.CASCADE)