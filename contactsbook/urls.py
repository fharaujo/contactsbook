from django.urls import path 

# meus imports - import views
from . import views

# padrão de "caminhos" da urls 
urlpatterns = [
    path('', views.index, name='index'),
    path('new-contact/', views.new_contact, name='new-contact'),
    path('profile/<str:pk>', views.contact_profile, name='profile'),
    path('edit-contact/<str:pk>', views.edit_contact, name='edit-contact'),
    path('delete/<str:pk>', views.delete_contact, name='delete')
 ]
 