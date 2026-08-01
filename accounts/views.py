from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import (
    CustomerRegistrationForm,
    FarmerRegistrationForm
)

from .models import User
from customers.models import Customer
from farmers.models import Farmer

def home(request):

    return render(
        request,
        'home.html'
    )

def register_customer(request):

    if request.method == 'POST':

        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.user_type = 'customer'

            user.save()

            Customer.objects.create(
                user=user
            )

            messages.success(
                request,
                'Customer account created successfully.'
            )

            return redirect('login')

    else:

        form = CustomerRegistrationForm()

    return render(
        request,
        'accounts/register_customer.html',
        {'form': form}
    )
    
def register_farmer(request):

    if request.method == 'POST':

        form = FarmerRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.user_type = 'farmer'

            user.save()

            Farmer.objects.create(
                user=user,
                farm_name="Pending",
                owner_name=user.username,
                phone="",
                email=user.email,
                address="",
                district="",
                state=""
            )

            messages.success(
                request,
                'Farmer registration submitted. Await admin approval.'
            )

            return redirect('login')

    else:

        form = FarmerRegistrationForm()

    return render(
        request,
        'accounts/register_farmer.html',
        {'form': form}
    )
    
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if user.user_type == 'farmer':

                farmer = Farmer.objects.get(user=user)

                if not farmer.is_approved:

                    messages.error(
                        request,
                        'Your account is awaiting approval.'
                    )

                    return redirect('login')

            login(request, user)

            if user.is_superuser:
                return redirect('admin_dashboard')

            elif user.user_type == 'farmer':
                return redirect('farmer_dashboard')

            elif user.user_type == 'customer':
                return redirect('all_products')

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(
        request,
        'accounts/login.html'
    )
    
def logout_view(request):

    logout(request)

    return redirect('login')





