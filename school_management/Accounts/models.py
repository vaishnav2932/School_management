import re
from django.contrib.auth.models import Permission,Group
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import ValidationError
from django.utils import timezone
import random
from django.core.validators import RegexValidator
import phonenumbers
from django.conf import settings
import uuid
from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    is_librarian = models.BooleanField(default=False)
    is_officestaff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    address = models.CharField(max_length=50)
    joining_date = models.DateField(null=True,blank=True)
    phone_number = models.CharField(max_length=15, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Fields required besides email and password

    obl= CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        related_name='app1_user_groups',  # Add a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    # Override user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='app1_user_permissions'  # Add a unique related_name
    )



    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    
class Librarian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='librarian')
    name = models.CharField(max_length=50,default="no name")
    shift_timing = models.CharField(max_length=50, blank=True, null=True)




class BookList(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genere = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

class Bookissued(models.Model):
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='librarian_isuued_book')
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_issed_book')
    book = models.ForeignKey(BookList, on_delete=models.CASCADE,related_name='issude_book')
    issude_date = models.DateField(auto_now_add=True)


class Office_staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='ofiice_staff')
    name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15, unique=True)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')    
    name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50, unique=True)

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField()
    last_payment_date = models.DateField(blank=True, null=True)
    is_fully_paid = models.BooleanField(default=False)    


class LibraryTransaction(models.Model):
    TRANSACTION_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]
    
    book = models.ForeignKey(BookList, on_delete=models.CASCADE, related_name='transactions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='library_transactions')
    staff = models.ForeignKey(Office_staff, on_delete=models.CASCADE, related_name='library_transactions')
    transaction_type = models.CharField(max_length=8, choices=TRANSACTION_CHOICES,db_index=True)
    transaction_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')


    