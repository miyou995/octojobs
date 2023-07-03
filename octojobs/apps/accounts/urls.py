from django.urls import path

from .views import create_client, only_clients_list

app_name= 'account'
urlpatterns = [
    path('only_clients_list/', only_clients_list, name="only_clients_list"),
]
