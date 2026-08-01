from django.urls import path
from . import views
from django.urls import path, include
urlpatterns = [
    path(
        'farmer-dashboard/',
        views.farmer_dashboard,
        name='farmer_dashboard'
    ),
]