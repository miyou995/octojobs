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
from .models import Job

# List Job View
class JobListView(ListView):
    template_name = 'job_list.html'
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context 

# Create Job View
class JobCreateView(CreateView):
    template_name = 'job_create.html'
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context 

# Update Job View
class JobUpdateView(UpdateView):
    template_name = 'job_update.html'
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
# Detail Job View
class JobDetailView(DetailView):
    template_name = 'job_detail.html'
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context 

# Delete Job View
class JobDeleteView(DeleteView):
    template_name = 'job_delete.html'
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context 