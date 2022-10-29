from django.urls import path, include
from quality import views

app_name="quality"
urlpatterns = [
    # path('create/', views.qualityCreate, name="create"),
    # path('<int:pk>/create/', views.qualityCreate, name="create"),
    path('<int:pk>/update/',views.qualityUpdate, name='update'),
    path('<int:pk>/', include([
        path('', views.qualityList, name="list"),
        path('create/', views.qualityCreate, name="create"),
        path('delete/', views.deleteQuality, name="delete"),
    ]))
    
]
