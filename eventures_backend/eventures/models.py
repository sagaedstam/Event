# eventures/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.apps import apps as django_apps
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, pre_save, pre_delete
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.dispatch import receiver

class MyUserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # def create_student(self, email, password=None, **extra_fields):
    #     """
    #     Create and save a student user with the given email and password.
    #     """
    #     extra_fields.setdefault('is_student', True)
    #     return self.create_user(email, password, **extra_fields)

    # def create_organization(self, email, password=None, **extra_fields):
    #     """
    #     Create and save an organization user with the given email and password.
    #     """
    #     extra_fields.setdefault('is_organization', True)
    #     return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('organization', 'Organization'), 
        ('admin', 'Admin')
    )
    username = None
    email = models.EmailField(null=False, max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, null=True)
    is_student = models.BooleanField(default= False)
    is_organization = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

class Student(models.Model):
    student = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="MyUser", on_delete=models.CASCADE, related_name='student', null=False)

    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)
    
    def __str__(self):
         return self.student.email

class Organization(models.Model):
    organization = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="MyUser", on_delete=models.CASCADE, related_name='organization', null=False)

    org_name = models.CharField(blank=False, null=False, max_length=255)
    
    def __str__(self):
         return self.org_name + '' + self.organization.email

@receiver(pre_save, sender=MyUser)
def UserName(sender, instance, **kwargs):
    try:
        instance.username = instance.email
    except Exception as e:
        print(str(e))

# class MyUser(AbstractUser):
#     USER_TYPE_STUDENT = 'student'
#     USER_TYPE_ORGANIZATION = 'organization'
#     USER_TYPE_CHOICES = [
#         (USER_TYPE_STUDENT, 'Student'),
#         (USER_TYPE_ORGANIZATION, 'Organization'),
#     ]

#     email = models.EmailField(max_length=100, unique=True)
#     user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default=USER_TYPE_STUDENT)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

# class Student(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
#     student_first_name = models.CharField(max_length=50)
#     student_last_name = models.CharField(max_length=50)
#     student_city = models.CharField(max_length=100)
#     student_phone = models.CharField(max_length=20)
#     student_allergies = models.CharField(max_length=200, blank=True)
#     student_drinking_preferences = models.CharField(max_length=200, blank=True)
#     created_at = models.DateTimeField(default=timezone.now, editable=False)
    
#     def __str__(self):
#         return f"{self.student_first_name} {self.student_last_name}"

#     class Meta:
#         verbose_name = 'Student'
#         verbose_name_plural = 'Students'

# class Organization(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
#     organization_name = models.CharField(max_length=255)
#     organization_description = models.TextField()
#     organization_city = models.CharField(max_length=255)
#     created_at = models.DateTimeField(default=timezone.now, editable=False)

#     def __str__(self):
#         return self.organization_name

#     class Meta:
#         verbose_name = 'Organization'
#         verbose_name_plural = 'Organizations'

