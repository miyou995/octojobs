from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView, 
    CreateView,
)
from apps.jobs.models import Job

# Create your views here.

class IndexView(ListView):
    model = Job
    template_name = 'index.html'
    