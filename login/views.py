from django.shortcuts import render,redirect
from .models import Department,Admin,Class,Student,Faculty,Course,Attendance,Teache
from django.contrib import messages
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

# views.py

def process_google_login(request):
    # Get the user's Google email
    print("hello============================================================================================")
    try:
        social_account = SocialAccount.objects.get(user=request.user, provider='google')
        google_email = social_account.extra_data['email']
    except SocialAccount.DoesNotExist:
        # Handle case where user hasn't connected Google account
        google_email = None
    print(google_email)
    # Implement your conditions here
    # For example, check if the email meets specific criteria
    if google_email and google_email.endswith('@example.com'):
        # Grant access to the user
        return render(request, 'grant_access.html', {'email': google_email})
    else:
        # Deny access
        return render(request, 'deny_access.html')
