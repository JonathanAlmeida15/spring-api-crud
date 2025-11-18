from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from clients.models import Client   # <-- SOMENTE ESTE IMPORT
from django.views.generic import UpdateView, DeleteView

def home(request):
    return render(request, 'dashboard/home.html')

class ClientListView(ListView):
    model = Client
    template_name = "dashboard/client_list.html"
    context_object_name = "clients"
    
class ClientCreateView(CreateView):
    model = Client
    fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'notes']
    template_name = "dashboard/client_form.html"
    success_url = reverse_lazy('dashboard:client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'notes']
    template_name = "clients/client_form.html"
    success_url = reverse_lazy('dashboard:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = "clients/client_confirm_delete.html"
    success_url = reverse_lazy("dashboard:client_list")