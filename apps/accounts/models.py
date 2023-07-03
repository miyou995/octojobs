from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, role, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, password, 'admin', **extra_fields)


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employer', 'Employer'),
        ('freelancer', 'Freelancer'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    username = None
    email = models.EmailField('email address', unique=True)
    picture = models.ImageField(upload_to='images/faces', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(verbose_name="Adresse", max_length=150, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def display_picture(self):
        if self.picture:
            return self.picture.url
        else: 
            return "/static/images/profile.png"

    @classmethod
    def create_user(cls, email, password, role, **extra_fields):
        manager = cls._default_manager
        return manager._create_user(email, password, role, **extra_fields)


class Employer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(_(""), max_length=50, blank=True, null=True)
