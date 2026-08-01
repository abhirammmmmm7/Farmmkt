from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from farmers.models import Farmer
from django.shortcuts import get_object_or_404, redirect

@login_required
def admin_dashboard(request):

    pending_farmers = Farmer.objects.filter(
        is_approved=False
    )

    approved_farmers = Farmer.objects.filter(
        is_approved=True
    )

    context = {
        'pending_farmers': pending_farmers,
        'approved_farmers': approved_farmers,
    }

    return render(
        request,
        'admin_panel/dashboard.html',
        context
    )


@login_required
def approve_farmer(request, farmer_id):

    farmer = get_object_or_404(
        Farmer,
        id=farmer_id
    )

    farmer.is_approved = True

    farmer.save()

    return redirect('admin_dashboard')