
from django.db import models
from users.models import CustomUser

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="profile_user")
    # TODO: I need to write "OneToOneField" there, as one user have only one profile.
    
    name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    
    city = models.CharField(max_length=50, null=True, blank=True)
    
    age = models.IntegerField(null=True, blank=True)
    
    designation = models.CharField(max_length=100, null=True, blank=True)
    exprience = models.IntegerField(null=True, blank=True)

    # we can also add profile_picture, links of media.