from django import forms
from .models import Job 


class OrderOutModelForm(forms.ModelForm):
    
    class Meta: 
        model = Job
        fields = (
                'title',
                'type',
                'category',
                'tags',
                'appliants',
                'status',
                'location',
                'description',
                'budget',
                'duration',
                'expiration',
                'deadline',
            )