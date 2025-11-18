from django.urls import path
from .views import home, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/new/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]
