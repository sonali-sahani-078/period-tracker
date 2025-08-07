from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Contact,CycleData
from datetime import datetime, timedelta
from django.db.models import Q

from .models import Contact



from django.utils.dateparse import parse_date  # Import this for messages


def index(request):
    return render(request, 'health/index.html')

def symptoms(request):
    return render(request, 'health/symptoms.html')
def healthtips(request):
    return render(request, 'health/healthtips.html')

def calendar_view(request):
    return render(request, 'health/calendar.html')

def contact(request):
    return render(request, 'health/contact.html')

@login_required
def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        en = Contact(Name=name, Email=email, Subject=subject, Message=message)
        en.save()  # Ensure this line is properly indented

    return render(request, 'health/contact.html')



# health/views.py
from django.shortcuts import render
from datetime import datetime, timedelta

def index(request):
    # Get current month and year
    today = datetime.today()
    month = today.month
    year = today.year

    # Get selected dates from POST request
    selected_dates = request.POST.getlist('dates') if request.method == 'POST' else []

    # Render the index template with month, year, and selected dates
    context = {
        'month': month,
        'year': year,
        'selected_dates': selected_dates
    }
    return render(request, 'health/index.html', context)
