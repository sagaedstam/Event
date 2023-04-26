# eventures/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a MyUser with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a MyUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('student', 'Student'),
        ('organization', 'Organization'), 
        ('admin', 'Admin')
    )
    email = models.EmailField(null=False, max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, null=True)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.is_staff

    @property
    def is_student(self):
        return self.user_type == 'student'

    @property
    def is_organization(self):
        return self.user_type == 'organization'


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    first_name = models.CharField(blank=False, null=True, max_length=255)
    last_name = models.CharField(blank=False, null=True, max_length=255)

    def __str__(self):
        return self.user.email


class Organization(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organization')
    org_name = models.CharField(blank=False, null=False, max_length=255)

    def __str__(self):
        return f'{self.org_name} ({self.user.email})'


@receiver(post_save, sender=MyUser)
def create_student_or_organization(sender, instance, created, **kwargs):
#     """
#     Create a Student or Organization instance when a new MyUser is created.
#     """
     if created and instance.is_student:
         Student.objects.create(user=instance)
     elif created and instance.is_organization:
         Organization.objects.create(user=instance)
