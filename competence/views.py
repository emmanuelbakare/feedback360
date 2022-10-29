from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.urls import reverse_lazy 
from django.views import generic
from competence.models import Competence, Bundle
from django.db.models.fields import Field 

from utils.build import EndPoints, get_model_fields
from utils.models import MakeModelOrQueryset
# Create your views here.

 
def getContext(obj_list=None, target="#obj_list",dtarget="#obj_list"):
    context={
        'object_list':obj_list,
        'name':'competence',
        'target':target,
        'delete_target':dtarget,
        'create':'competence:bundle-create',
        'retrieve':'quality:list',
        'update':'competence:update',
        'delete':'competence:delete',
    }
    
    return context     

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
        competence=endpoints.model_object
        competence.name=request.POST.get('obj_name')
        competence.save()
        endpoints.new_path('obj2', competence)
        return render(request, 'comp_qty/item.html', endpoints.context)    
    return render(request, 'comp_qty/update.html', context)

# def competenceUpdate(request,pk=None):
#     competence=Competence.objects.get(pk=pk)
#     context=getContext(target="#child_list")
#     context['obj2']=competence
#     print('CONTEXT BEFORE UPDATE', context)
#     if request.method=="POST":
#         competence.name=request.POST.get('obj_name')
#         competence.save()
#         print('CONTEXT AFTER UPDATE', context)
#         return render(request, 'comp_qty/item.html', context)    
#     return render(request, 'comp_qty/update.html', context)
    
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
    if request.htmx:
        return render(request, 'comp_qty/list.html', context)
    return  render(request, 'comp_qty/home.html', context)
 

def table_comp(request):
    competences=Competence.objects.all()
    endpoints=EndPoints(competences, defaults=True)
    
    # model header -- retrieve only the fields in the model
    # headers=[field.name for field in Competence._meta.get_fields() if isinstance(field, Field)]
    headers=get_model_fields(Competence)
    endpoints.new_path('headers', headers)

    context=endpoints.context
    print('CONTEXT', context)
    return render(request, 'table/table.html', context)


# def get_model_fields(cls):
#     fields=cls._meta.get_fields()
#     return [field.name for field in fields if isinstance(field, Field)]
 
 

