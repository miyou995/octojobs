from django.db import models
from django.utils.translation import gettext as _

from django.conf import settings
from tinymce import models as tinymce_models

# Create your models here.
JOB_TYPE_CHOICES = (
    ("FULLTIME", _("Full Time")),
    ("PART_TIME", _("Part Time")),
    ("FREELANCER",_("Freelancer")),
    ("INTERNSHIP", _("Internship")),
    ("TEMPORARY", _("Temporary")),
)
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
JOB_CATEGORY_CHOICES = (
    ("ACCOUNTING_AND_FINANCE", _("Accounting and Finance")),
    ("CLERICAL_&_DATA_ENTRY", _("Clerical & Data Entry")),
    ("COUNSELING",_("Counseling")),
    ("COURT_ADMINISTRATION", _("Court Administration")),
    ("HUMAN_RESOURCES", _("Human Resources")),
    ("INVESRIGATIVE", _("Investigative")),
    ("IT_AND_COMPUTERS", _("IT and Computers")),
    ("LAW_ENFORCEMENT",_("Law Enforcement")),
    ("MANAGEMENT", _("Management")),
    ("PUBLIC_RELATIONS", _("Public Relations")),
)
    




#class Category(models.Model):
 #   parent  = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
  #  is_active =  models.BooleanField(default=True)
    #name = models.CharField(max_length=50)
    #created         = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    #updated         = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    #def __str__(self):
     #   return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    is_active =  models.BooleanField(default=True)
    created         = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated         = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)


#class Type(models.Model):
 #   parent  = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
  #  is_active =  models.BooleanField(default=True)

   # name = models.CharField(max_length=50)
    ##created         = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    #updated         = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    #def __str__(self):
     #   return str(self.name)
class Job(models.Model):
    title       = models.CharField( verbose_name=_("job title"), max_length=150)
    type        = models.CharField(choices=JOB_TYPE_CHOICES, default="FREELANCER",max_length=20, verbose_name=_("Job type")) # on Job Model
    category    =  models.CharField(choices=JOB_CATEGORY_CHOICES, default="ACCOUNTING_AND_FINANCE",max_length=50, verbose_name=_("Job category"))
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

