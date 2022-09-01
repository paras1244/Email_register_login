
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.conf import settings

# if you need to create full user model by your self then need to override "AbstractBaseUser"
# I am doung updation on user model with  "AbstractUser".

class CustomUser(AbstractUser):
    username = None                 # removing username, first_name and last_name as we not need for now
    first_name = None
    last_name = None
    email = models.EmailField(('email address'), unique=True)
    
    USER_TYPE_CHOICES = (
        ("ADMIN_USER", "Admin_User"),
        ("SOLUTION_PROVIDER", "Solution_Provider"),
        ("SOLUTION_SEEKER", "Solution_Seeker"),
    )
    
    user_type = models.CharField(max_length=18, choices=USER_TYPE_CHOICES, default="SOLUTION_SEEKER")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="testing Forgot Password API"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
        fail_silently=False,
    )