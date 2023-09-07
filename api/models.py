from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    User Profile Model

    This model is used to extend the default Django User model.

    Attributes:
        slack_name (str): The slack name of the user.
        track (str): The track the user is on.

    Exanple:
    
            {
              "slack_name": "example_name",
              "track": "backend",
            }
    """
    slack_name = models.CharField(max_length=50, unique=True)
    track = models.CharField(max_length=50)

    USERNAME_FIELD = 'slack_name'

    def __str__(self):
        return self.slack_name

    def __repr__(self):
        return f"<User: {self.slack_name}, Track: {self.track}>" 

