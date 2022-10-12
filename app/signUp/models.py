from django.db import models
# To validate users
from django.contrib.auth.models import User


# A model class of user accounts
class Account(models.Model):

    # Instance for user validation(1vs1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Adding fealds
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
