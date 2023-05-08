from django.db import models
from django.contrib.auth.hashers import check_password
from django.db.models import Q


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    logged_in = models.BooleanField(default=False)

    @classmethod
    def authenticate(cls, username_or_email, password):
        users = cls.objects.filter(Q(email=username_or_email) | Q(username=username_or_email))
        if users:
            user = users.first()
            if check_password(password, user.password):
                return user

    def login(self, request):
        self.logged_in = True
        self.save()
        request.session['user'] = {'pk': self.pk, 'username': self.username, 'email': self.email}

    def logout(self, request):
        self.logged_in = False
        self.save()
        request.session['user'] = None

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Users'
