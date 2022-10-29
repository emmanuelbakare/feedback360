from django.http import HttpResponse
from django.shortcuts import render
from quality.models import Quality
from competence.models import Competence

# Create your views here.

def qualityList(request, pk, target="#child_list"):
    ''' get all qualities associated with a competence identified by its pk
    create a context containing all the qualities, the competence object and the
    action button urls'''
    # qualities=Quality.objects.filter(competence=pk)
    competence=Competence.objects.get(pk=pk)
    context={
        'object_list':competence.qualities.all(),
        'name':'quality',
        'other_obj':competence,
        "target":target,
        'create':'quality:create',
        'requireid':True,
        'update':'quality:update',
        'delete':'quality:delete',
    }
    return render(request,'comp_qty\list.html', context)


def qualityCreate(request,pk=None):
    ''' Create a quality attached to a competence
    1. get the quality 
    2. create the quality and attached it to its competence 
    3.return the new qualities '''
    name=request.POST.get('form_name')
    competence=Competence.objects.get(pk=pk)
    quality=Quality.objects.create(name=name, competence=competence)
    return qualityList(request, pk)
    
    # return qualityList(request, pk)
   

def deleteQuality(request,pk):
    ''' get the quality to delete and then issue the delete command on it
    then relist all the remaining qualities'''
    quality=Quality.objects.get(pk=pk) 
    pk=quality.competence.pk
    quality.delete()
    return qualityList(request,pk)

def qualityUpdate(request,pk=None):
    ''' update an existing quality - this view first returns the form for updating
    and after update button is clicked, it updates the record and 
    return the li showing the updated list item
    it passes the context that contains the update, delete url to the li update and delete btn'''
    quality=Quality.objects.get(pk=pk)
    context={'obj2':quality, 
            'name':'quality',
            'update':'quality:update',
            'delete':'quality:delete',
    }
    
    print('CONTEXT',context)
    if request.method=="POST":
        quality.name=request.POST.get('obj_name')
        quality.save()
        return render(request, 'comp_qty/item.html', context)
    return render(request, 'comp_qty/update.html', context)
# def qualityUpdate(request,pk=None):
#     ''' update an existing quality - this view first returns the form for updating
#     and after update button is clicked, it updates the record and 
#     return the li showing the updated list item
#     it passes the context that contains the update, delete url to the li update and delete btn'''
#     quality=Quality.objects.get(pk=pk)
#     if request.method=="POST":
#         quality.name=request.POST.get('obj_name')
#         quality.save()
#         context={'obj':quality, 
#                  'name':'quality',
#                  'update':'quality:update',
#                  'delete':'quality:delete',
#                  }
#         return render(request, 'comp_qty/item.html', context)    
#     context={'obj':quality, 
#              'name':'quality',
#              'update':'quality:update',
#             'delete':'quality:delete',
#              }
#     return render(request, 'comp_qty/update.html', context)