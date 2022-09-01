


from django.urls import path
from .views import ProfileView
# UserDetailAPI

urlpatterns = [
    path('profile/',ProfileView.as_view()),     # POST and GET
]
