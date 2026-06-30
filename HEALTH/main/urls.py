from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('appointment', views.appointment, name='appointment'),
    path('feature', views.feature, name='feature'),
    path('team', views.team, name='team'),
    path('service', views.service, name='service'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('error', views.error, name='error'),
]