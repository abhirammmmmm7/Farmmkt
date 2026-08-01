from django.urls import path
from . import views

urlpatterns = [
    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),
    
    path(
    'approve-farmer/<int:farmer_id>/',
    views.approve_farmer,
    name='approve_farmer'
),
]

