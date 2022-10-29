from django.http import HttpResponse
from django.shortcuts import render 
from competence.models import  Bundle, Competence
import json 
#HOME
def getContext(obj_list=None, target="#obj_list",dtarget="#obj_list"):
    
    context={
        'object_list':obj_list,
        'name':'bundle',
        'target':target,
        'delete_target':dtarget,
        'create':'competence:bundle-create',
        'retrieve':'competence:bundle-retrieve',
        'update':'competence:bundle-update',
        'delete':'competence:bundle-delete',
    }
    
    return context


def bundlesHome(request):
    context={
        'object_list':Bundle.objects.all(),
        'name':'bundle',
        'create':'competence:bundle-create',
    }
    return render(request, 'comp_qty/home.html', context)

#CREATE BUNDLE
def bundle_create(request):
    ''' Create a bundle- Bundles contains lists of competences'''
    name=request.POST.get('form_name')
    Bundle.objects.create(name=name)
    return bundle_list(request)
  
def bundle_list(request, target="#child_list"):
    bundles=Bundle.objects.all()
    context=getContext(bundles,target=target)
    if request.htmx:
        return render(request, 'comp_qty/list.html', context)
    return render(request, 'competence/bundle/home.html', context)
 
def bundle_update(request,pk):
    bundle=Bundle.objects.get(pk=pk)
   
    context=getContext()
    context['obj2']=bundle
    context['target']="#child_list"
        
    if request.method=="POST": # after clicking the update button run this code block
        bundle.name=request.POST.get('obj_name')
        bundle.save()
        print('CONTEXT AFTER SAVE', context)
        return render(request, 'comp_qty/item.html', context)
    return render(request, 'comp_qty/update.html', context)
    
def bundle_delete(request,pk):
    bundle=Bundle.objects.get(pk=pk)
    bundle.delete()
    return bundle_list(request)

 # BUNDLE COMPETENCES 
 
def bundle_retrieve(request,pk=None, bundle=None,dtarget="#child_list"):
    '''when a bundle is clicked (from the list displated), this retrieves all the competences 
    that is in the bundle the value is displayed in a dropdown list. '''
    if not bundle:
        bundle=Bundle.objects.get(pk=pk) # get selected bundle
    bundle_competences=bundle.competences.all() # get all competences in this bundle
   
    #get all the competences that is not part of this bundle
    remaining_comps=Competence.objects.all().exclude(pk__in=bundle.competences.all())
                   
    context=getContext(bundle_competences,dtarget=dtarget)
    context['remaining_comps']=remaining_comps
    context['obj']=bundle
    context['create']=None
    # context['retrieve']='competence:bundle-competence-list'
    context['retrieve']=None
    context['update']=None
    context['delete']='competence:bundle-competence-remove'
    if request.method=="POST":
        '''retreive the selected competence and add it to this bundle'''
        new_competence=Competence.objects.get(pk=request.POST.get('comps'))
        bundle.competences.add(new_competence)
        # return render(request, 'competence/bundle/partials/list.html', context)

    #create the context to pass to the template
    return render(request, 'competence/bundle/partials/list.html', context)
    
def bundle_competences_add(request,pk):
    new_competence=Competence.objects.get(pk=request.POST.get('comps'))
    bundle=Bundle.objects.get(pk=pk).competences.add(new_competence)
    return bundle_list(request) 

    
def bundle_competence_remove(request,competenceid):
    '''remove a competence from a bundle'''
    print('REQUEST BODY', request.get_full_path())
    # request.body returns b'parent_obj=<int>' use .decode() to make it str and split to get the int
    parentstr=request.body.decode().split('=')[1]  
    bundleid=int(parentstr)
    
    competence_to_remove=Competence.objects.get(pk=competenceid)
    bundle=Bundle.objects.get(pk=bundleid)
    bundle.competences.remove(competence_to_remove)
    return bundle_retrieve(request,bundle=bundle,dtarget="#child_list")
   
