from django.urls import path
from . import views

#### localhost:8000/studyplan/indexpage
urlpatterns = [
    # path('indexpage', views.index),
    # path('sample', views.sample)

     # path('<page>', views.pages),
     path('home', views.home),
     path('getData', views.display)
]