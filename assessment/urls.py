from django.urls import path 
from assessment import views 

app_name="assessment"
urlpatterns=[
    path('', views.assessments, name="list"),
    path('test/', views.asmtPost, name="post"),
    path('create/', views.assessmentForm, name="createform"),
]