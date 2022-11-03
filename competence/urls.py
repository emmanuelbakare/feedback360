from django.urls import path, include 
from competence import views
from competence import views_bundles
# from competence import api
# from competence.api import views as apiviews

app_name="competence"
urlpatterns = [
    # path('', views.CompetenceList.as_view(), name="competence"),
    path('', views.competenceList, name="competence"),
    path('api/', include('competence.api.urls')),

    path('create/', views.competenceCreate, name="create"),
    path('test2/', views.comptest2, name="comptest2"),
    path('table/', views.table_comp, name="table-comp"),
    path('table/<int:pk>/', views.table_qty, name="table_qty"),



    # path('endpoints/', views.get_endpoints, name="endpoints"), 
    
    path('<int:pk>/', include([
        path('', views.competenceUpdate, name='update'),
        path('delete/', views.deleteCompetence, name="delete"),
    ])),
    
    # COMPETENCE BUNDLES--
    path('bundles/',include([
        path('', views_bundles.bundle_list, name='bundles'),
        path('create/', views_bundles.bundle_create, name='bundle-create'), # create a new bundle
        path('<int:pk>/delete/', views_bundles.bundle_delete, name='bundle-delete'),
        path('<int:pk>/update/', views_bundles.bundle_update, name='bundle-update'),
        path('<int:pk>/retrieve/', views_bundles.bundle_retrieve, name='bundle-retrieve'),
        
        path('<int:pk>/add/', views_bundles.bundle_competences_add, name='bundle-competences-add'),
        path('competence/<int:competenceid>/delete/', views_bundles.bundle_competence_remove, name='bundle-competence-remove'),
        # path('<int:bundleid>/competence/<int:competeceid>/', views_bundles.bundle_competence_remove, name='bundle-competence-remove'),
        
        # path('<int:pk>/', views_bundles.bundle_competences, name='bundle-competences'),
           
    ])),
    
]


#HTMX
urlpatterns+=[
    path('list/', views.competenceList, name="list"),
]