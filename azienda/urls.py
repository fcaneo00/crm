from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),
    path('new/store/', views.store, name='store')
]
