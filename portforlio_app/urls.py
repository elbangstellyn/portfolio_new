from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('project/detail/<int:pk>/', views.detailProjectView, name='detail'),
    path('projects/', views.projectview, name='projects'),
    path('download/<int:pk>/', views.download, name='download'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
