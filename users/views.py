from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from users.models import User


def registerUser(request):
    if request.method == 'POST':
        error_messages = {}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('confirm-password')

        if min(len(password), len(password_confirm)) < 8:
            error_messages['password_error'] = 'Note: Password should have more than 8 characters!'
        if password != password_confirm:
            error_messages['password_error'] = 'Note: Password don\'t match!'

        if error_messages:
            return render(request, 'users/register.html', error_messages)

        user, created = User.objects.get_or_create(username=username, email=email, defaults={'password': make_password(password)})
        if not created:
            error_messages['email'] = 'Note: User with this email already exists!'
            return render(request, 'users/register.html', error_messages)

        return redirect(reverse('users:login'))
    elif request.method == 'GET':
        return render(request, 'users/register.html')


def loginUser(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        user = User.authenticate(username_or_email, password)
        if user:
            user.login(request)
            return redirect(reverse('home'))
        return render(request, 'users/login.html', context={'error': 'Credentials don\'t match'})
    return render(request, 'users/login.html')


def logoutUser(request, pk):
    User.objects.get(pk=pk).logout(request)
    return redirect(reverse('home'))

