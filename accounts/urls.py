from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    
    path(
        '',
        views.home,
        name='home'
        ),
    
    path(
        'login/',
        views.login_view,
        name='login'
    ),
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
    path(
        'register/customer',
        views.register_customer,
        name='register_customer'
    ),
    path(
        'register/farmer',
        views.register_farmer,
        name='register_farmer'
    ),
]
    