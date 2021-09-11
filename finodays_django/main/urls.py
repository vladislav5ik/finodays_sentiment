from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create_chat', views.create_chat, name='create_chat'),
    path('check_sentiment', views.check_sentiment, name='check_sentiment')
]
