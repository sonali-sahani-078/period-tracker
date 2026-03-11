from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Contact


def index(request):
    today = datetime.today()
    context = {
        "month": today.month,
        "year": today.year,
    }
    return render(request, "health/index.html", context)


def symptoms(request):
    return render(request, "health/symptoms.html")


def healthtips(request):
    return render(request, "health/healthtips.html")


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            subject=request.POST.get("subject", "").strip(),
            message=request.POST.get("message", "").strip(),
        )
        messages.success(request, "Your message has been sent successfully.")
        return redirect("contact")

    return render(request, "health/contact.html")
