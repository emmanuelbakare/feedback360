from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.urls import reverse_lazy 
from django.views import generic
from competence.models import Assessment, Competence, Bundle
from quality.models import Quality
from django.db.models.fields import Field 

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from utils.build import EndPoints
from utils.models import MakeModelOrQueryset, get_model_fields
# Create your views here.

 
# def getContext(obj_list=None, target="#obj_list",dtarget="#obj_list"):
#     context={
#         'object_list':obj_list,
#         'name':'competence',
#         'target':target,
#         'delete_target':dtarget,
#         'create':'competence:bundle-create',
#         'retrieve':'quality:list',
#         'update':'competence:update',
#         'delete':'competence:delete',
#     }
    
#     return context     

def competenceCreate(request):
    if request.method=="POST":
        name=request.POST.get('form_name')
        competence=Competence.objects.create(name=name)
        return competenceList(request)
    
 


def competenceUpdate(request,pk=None):
    competence=Competence.objects.get(pk=pk)
    endpoints=EndPoints(competence, pk=pk, defaults=True)
    # endpoints=EndPoints("competence", pk=pk, defaults=True)
    endpoints.new_path('retrieve','quality:list')
    context=endpoints.context

    if request.method=="POST": 
        # competence=endpoints.model_object
        competence.name=request.POST.get('obj_name')
        competence.save()
        endpoints.new_path('obj2', competence)
        endpoints.new_path('target','#child_list')
        return render(request, 'comp_qty/item.html', endpoints.context)    
        # return render(request, 'comp_qty/item.html', endpoints.context)    
    return render(request, 'comp_qty/update.html', context)


    
def deleteCompetence(request, pk):
    competence=Competence.objects.get(pk=pk)
    competence.delete()
    return competenceList(request)
    
def competenceList(request, target="#child_list", dtarget="#obj_list" ):
   
    endpoints=EndPoints("competence",defaults=True)
    endpoints.new_path('target',target)
    endpoints.new_path('create','competence:create') 
    endpoints.new_path('delete_target',dtarget)
    endpoints.new_path('retrieve','quality:list')
    context=endpoints.context
    # print('LIST CONTEXT', context)
    if request.htmx:
        return render(request, 'comp_qty/list.html', context)
    return  render(request, 'comp_qty/home.html', context)
 

def table_comp(request):
    competences=Competence.objects.all()
    endpoints=EndPoints(competences,  defaults=True)
    
    # model header -- retrieve only the fields in the model
    headers=get_model_fields(Competence, show=[ 'name','created','modified']) # show specific fields (name, created, modified)
    endpoints.new_path('headers', headers) 
    endpoints.new_path('target','#tab_disp')  # add 'target' as location to display the rendered result 
    endpoints.new_path('table_classes','table table-striped table-secondary')
    endpoints.new_path('retrieve','competence:table_qty') # when a table item is clicked, run the view in competence:table_qty url
    # endpoints.remove_path('create')
    context=endpoints.context
    print('CONTEXT TABLE COMPETENCE', context)
    return render(request, 'table/home.html', context)

def table_qty(request, pk=None):

    qualities=Quality.objects.filter(competence__id=pk)

    endpoints=EndPoints(qualities)

    headers=get_model_fields(qualities, show=['name','created']) # retrieve the fields to display 
    endpoints.new_path('headers',headers) # add the fields to the context dict to pass to the rendering html template
    endpoints.new_path('table_classes','table table-striped table-bordered') # style the table used to display the result
    # endpoints.new_path('delete', 'quality:delete')
    context=endpoints.context  # generate the context dictionary
    print('CONTEXT TABLE QUALITY', context)

    if request.htmx:        
        return render(request, 'table/table.html', context)  # ass the context dict to table.html which will render the result
    return HttpResponse("feedback")

     



