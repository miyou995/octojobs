from django.db import models
from django.utils.translation import gettext as _

from django.conf import settings
from tinymce import models as tinymce_models

# Create your models here.
# JOB_TYPE_CHOICES = (
#     ("FULLTIME", _("Full Time")),
#     ("PART_TIME", _("Part Time")),
#     ("FREELANCER",_("Freelancer")),
#     ("INTERNSHIP", _("Internship")),
#     ("TEMPORARY", _("Temporary")),
# )
# type        = models.CharField(choices=JOB_TYPE_CHOICES, default="FREELANCER", verbose_name=_("Job type")) # on Job Model

BUDGET_CHOICES = (
    (1, "0 - 5 000"),
    (2, "5 000 - 10000"),
    (3, "10000 - 100000"),
    (4, "+100 000"),
)
STATUS_CHOICES = (
    ("PENDING", _("Pending")),
    ("ACTIF", _("Actif")),
    ("CANELED", _("Canceled")),
    ("ALLOCATED",_("Allocated")),
    ("CLOSED", _("Closed")),
)



class Category(models.Model):
    parent  = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    is_active =  models.BooleanField(default=True)

    name = models.CharField(max_length=50)
    created         = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated         = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    is_active =  models.BooleanField(default=True)
    created         = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated         = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)



class Job(models.Model):
    title       = models.CharField( verbose_name=_("job title"), max_length=150)
    slug        = models.CharField( verbose_name=_("job url"), max_length=150)
    category    = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    tags        = models.ManyToManyField(Tag, verbose_name=_("tags"))
    appliants   = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Application')
    status      = models.CharField(choices=STATUS_CHOICES, default="PENDING", verbose_name=_("Status type"), max_length=20)
    location    = models.ForeignKey("core.Commune", verbose_name=_(""), on_delete=models.CASCADE)
    description   = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)

    budget      = models.PositiveSmallIntegerField(choices=BUDGET_CHOICES, default=1, verbose_name="Type de commande")
    duration    = models.IntegerField(verbose_name=_("Number of days"), null=True, blank=True)
    expiration  = models.DateField(blank=True, null=True)
    deadline    = models.DateField(blank=True, null=True)
    is_active =  models.BooleanField(default=False)

    created     = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated     = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    def __str__(self):
        return str(self.title)

class Application(models.Model):
    job         = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    selected    = models.BooleanField(default=False)
    created     = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated     = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

