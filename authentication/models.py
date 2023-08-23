import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

ROLE_CHOICES = (
    (0, 'staff'), #people who could vote for the day menu
    (1, 'restauranter'), #those people who will create and manage restaurant or several of them
)

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)

    email = models.CharField(max_length=100, unique=True, default=None)

    password = models.CharField(default=None, max_length=255)
    created_at = models.DateTimeField(editable=False, auto_now_add=datetime.datetime.now(), blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=datetime.datetime.now(), blank=True, null=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.id}-{self.email}"

    def __repr__(self):
        return f"{CustomUser.__name__}(name={self.email})"

    class Meta:
        ordering = ('id',)
        app_label = 'authentication'


