from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from pprint import pprint
from django.views.decorators.csrf import csrf_protect

from .models import Application





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
  



def job_application(request, job_id):
    print('job application ====================')
        
    if request.user.is_authenticated:
        user = request.user
        job  = get_object_or_404(Job,  id=job_id)
        Application.objects.create(job=job, applicant=user)
        print(f"user :  {user.email} subscribed to job:{job}")
    else:
        print('user is not authenticated')
    return redirect("jobs:job_list")


  

    
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
    pk_url_kwarg = 'id'
    def get(self, request, id):
        job_courant = Job.objects.get(pk=id)
        objets_similaires = Job.objects.filter(budget=job_courant.budget, created=job_courant.created)

        context = {
            'job_courant': job_courant,
            'objets_similaires': objets_similaires
        }

        return render(request, 'jobs/job_detail.html', context)


    # context_object_name = "job"

    #def apply_now(self, request, *args, **kwargs):
        #if request.method == 'POST':
           # name = request.POST.get('name')
            #email = request.POST.get('emailaddress')
           # cv_file = request.FILES.get('upload-cv')
            #application = Application(name=name, email=email, cv_file=cv_file)
           # application.save()
           # return redirect('success_page')  # Rediriger vers une page de réussite
        #return render(request, 'apply_now.html')  # Afficher le formulair
       





    

# Delete Job View
class JobDeleteView(DeleteView):
    template_name = 'jobs/job_delete.html'
    model = Job


  
