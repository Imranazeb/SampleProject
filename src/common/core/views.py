from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render


@login_required
def home(request):
    return render(request, "core/home.html")


def send_test_email(request):
    send_mail(
        "Test Email",
        "This is a test email sent from Django using MailHog.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
    return HttpResponse("Test email sent.")
