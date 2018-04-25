from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    # Example: /search/
    path('', views.Home.as_view(), name="index"),
]
