from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.faketest ),
    path('competence/<int:totalrecord>/', views.fakeCompetence ),
    path('qualities/<int:totalrecord>/', views.fakeQualities ),
    path('qualities2/<int:totalrecord>/', views.fakeQualities2 ),
    
    path('bundle/<int:totalrecord>/', views.fakeBundle ),
    path('cbundle/<int:totalrecord>/', views.fakeBundleCompetence ),
]
