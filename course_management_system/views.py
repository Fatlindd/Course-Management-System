from django.shortcuts import render, redirect
from django.urls import reverse

from users.models import User


def home(request):
    # if not request.session.get('user'):
    #     return redirect(reverse('users:login'))
    return render(request, 'base.html')
