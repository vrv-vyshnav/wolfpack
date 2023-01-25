from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('user/',userView.as_view()),
    path('register/',RegisterView.as_view()),
    path('img/',ImageView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
