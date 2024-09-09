# chatapp/urls.py
from django.urls import path
from .views import chat_gpt

urlpatterns = [
    path('', chat_gpt, name='chat_gpt'),
]
