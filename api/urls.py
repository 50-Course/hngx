from django.urls import path
from .views import SlackUserView


urlpatterns = [
    path('v1/', SlackUserView.as_view(), name='user-view'),
]
