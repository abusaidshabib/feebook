from django.db import models
from authentication.models import BaseModel, CustomUser

class Message(BaseModel):
    message = models.CharField(max_length=255)
    from_user = models.ForeignKey(CustomUser, related_name="from_massage", on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name="to_massage", on_delete=models.CASCADE)

class ENotification(BaseModel):
    notification = models.CharField(max_length=255)
    isCheck = models.BooleanField()
    user = models.ForeignKey(CustomUser, related_name="notification", on_delete=models.CASCADE)

