from django.urls import path
from .views import chatbot_response
from . import views

urlpatterns = [
    path('chatbot/', chatbot_response, name='chatbot_response'),
    path('', views.chat, name='chat'),
]
