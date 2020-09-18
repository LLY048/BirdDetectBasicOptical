from django.urls import path
from . import views

urlpatterns = {
    path('birdCheck0915', views.birdCheck0915, name='birdCheck0915')
}