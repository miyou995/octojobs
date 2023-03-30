from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext as _
from django.conf import settings
from django.urls import reverse

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
        first_name
        last_name
        email
        is_staff
        is_active
        date_joined
    """
    # base_role   = Role.ADMIN
    # role        = models.CharField(max_length=50, choices=Role.choices)
    username    = None
    email       = models.EmailField('email address', unique=True)
    
    picture     = models.ImageField(upload_to='images/faces', null=True, blank=True)
    phone       = models.CharField(max_length=20, null=True, blank=True)
    address      = models.CharField(verbose_name="Adresse", max_length=150, null=True, blank=True)
    # role        = models.CharField(max_length=50, choices=Role.choices,  default=base_role)
    # warehouse = models.ForeignKey(WareHouse, on_delete=models.SET_NULL, related_name='managers',blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    # class Meta:
    #     abstract = True
        # app_label = 'account'


    def save(self, *args, **kwargs):
        # if not self.pk:
        #     self.type = self.base_role
        return super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs={"username": self.username})

    @property
    def display_picture(self):
        if self.picture:
            return self.picture.url
        else: 
            return "/static/images/profile.png" 
        

class Employer(models.Model):
    user    = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(_(""), max_length=50, blank=True, null=True)
    website = models.URLField(_(""), max_length=200, blank=True, null=True)



class Freelancer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
