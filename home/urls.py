from django.urls import path
from . import views

urlpatterns = [
    # Example: /search/
    path('', views.Home.as_view()),
]
