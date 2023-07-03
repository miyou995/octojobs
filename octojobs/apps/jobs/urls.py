from django.urls import path
from .views import JobListView, JobCreateView, JobDeleteView, JobDetailView, JobUpdateView

from .views import *

app_name= 'jobs'
urlpatterns = [
    path('',JobListView.as_view(), name='job_list'),
    path('create', JobCreateView.as_view(), name='job_create'),
    path('update/<int:pk>', JobUpdateView.as_view(), name='job_update'),
    path('detail/<int:pk>', JobDetailView.as_view(), name='job_detail'),
]
