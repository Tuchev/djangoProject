from django.urls import path

from djangoProject.tasks.views import home

# App
urlpatterns = (
    path('', home),
)
