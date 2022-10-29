from django.shortcuts import render
from assessment.forms import AssessmentForm
from competence.models import Assessment
from django.urls import reverse
from django.http import HttpResponseRedirect

def assessments(request):
    assessments=Assessment.objects.all()
    form=AssessmentForm(request.POST or None)
    context={
        'assessments':assessments,
        'form': form
    }
    if request.method=="POST":
        print('DATA POSTED', request.POST)
        if form.is_valid():
            newrec=form.save(commit=False)
            newrec.assessor=request.user 
            newrec.save()
            return HttpResponseRedirect(reverse('assessment:list'))
        else:
            return HttpResponse("Assessment NOT Created")
        
    return render(request, 'assessment/list.html', context)

from django.http import HttpResponse
def asmtPost(request):
    print('REQUEST DATA', request)
    # return render(request, 'assessment/list.html', {'form':}) 
    return HttpResponse("")

def assessmentForm(request):
    if request.method=="POST":
        form=AssessmentForm(request.POST)
        
        if form.is_valid():
            
            newrec=form.save(commit=False)
            newrec.assessor=request.user 
            newrec.save()
        
    form=AssessmentForm()
    context={'form':form}
    return render(request,'assessment/index.html', context )
