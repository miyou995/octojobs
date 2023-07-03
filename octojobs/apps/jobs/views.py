from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from pprint import pprint
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView, 
    CreateView,
    TemplateView
)
from .models import Job
from apps.core.models import Commune
# List Job View
class JobListView(ListView):
    template_name = 'jobs/job_list.html'
    model = Job

    
# Create Job View
class JobCreateView(CreateView):
    template_name = 'jobs/job_create.html'
    model = Job
    fields='__all__'
         

    def get_context_data(self, **kwargs):
        context = super(JobCreateView, self).get_context_data(**kwargs)
        context["communes"] = Commune.objects.all()
      

        return context
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        print("hello", form)
        return response    
class SignupsuccessView(TemplateView):
    template_name = "jobs/job_create.html" 



 

# Update Job View
class JobUpdateView(UpdateView):
    template_name = 'jobs/job_update.html'
    model = Job


    
# Detail Job View
class JobDetailView(DetailView):
    template_name = 'jobs/job_detail.html'
    model = Job

    

# Delete Job View
class JobDeleteView(DeleteView):
    template_name = 'jobs/job_delete.html'
    model = Job

    