from django.urls import path  
from accounts import views, forms
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name='accounts'
urlpatterns = [
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
    
    path('login/',views.CustomLoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('upload/', views.uploadphoto, name="uploadphoto")
]
 


