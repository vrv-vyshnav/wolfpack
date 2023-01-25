from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('user/',userView.as_view()),
    path('register/',RegisterView.as_view()),
    path('img/',ImageView.as_view()),
]
