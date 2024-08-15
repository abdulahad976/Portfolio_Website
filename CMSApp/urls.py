from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success_page'),  # Add your success page here

]

