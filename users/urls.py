
from django.urls import path, include
from .views import ChangePasswordView, LoginWithEmail, RegisterUserAPIView

urlpatterns = [
    path('register/',RegisterUserAPIView.as_view()),
    path('login/',LoginWithEmail.as_view()),
    
    # change_password
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),

    # Forgot password.
    path('forgot_password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
