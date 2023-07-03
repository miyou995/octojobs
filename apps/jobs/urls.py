from django.urls import path
from .views import JobListView, JobCreateView, JobDeleteView, JobDetailView, JobUpdateView, job_application

from .views import *

app_name= 'jobs'
urlpatterns = [
    path('list/',JobListView.as_view(), name='job_list'),
    path('create', JobCreateView.as_view(), name='job_create'),
    path('update/<int:id>', JobUpdateView.as_view(), name='job_update'),
    path('detail/<int:id>', JobDetailView.as_view(), name='job_detail'),
    path('apply-for-job/<int:job_id>', job_application, name='job_application'),
]
