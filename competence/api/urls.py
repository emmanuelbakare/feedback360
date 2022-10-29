from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import CompetenceViewset


router=DefaultRouter()
router.register('',CompetenceViewset )

urlpatterns = [

    path('', include(router.urls))

]