
from django.urls import path
from .views import SlackUserAPIView


urlpatterns = [
    path('', SlackUserAPIView.as_view(), name='user-view'),
]
