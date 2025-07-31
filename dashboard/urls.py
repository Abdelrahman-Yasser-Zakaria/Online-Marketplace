from django.urls import path  # type: ignore
from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.index, name="index"),
]
