from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Member_signup.as_view())
]