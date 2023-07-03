from django.urls import path, include
from .views import IndexView

from .views import *

app_name= 'apps.core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
