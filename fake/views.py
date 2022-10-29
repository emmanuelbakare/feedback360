from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
from competence.models import Competence, Bundle
from quality.models import Quality
import random

# Create your views here.
def faketest(request):
    # return HttpResponse('<h1>testing fake</h1>')
    return render(request, 'test.html')

def fakeCompetence(request,totalrecord):
    fake=Faker()
    records=""
    for k in range(totalrecord):
        competence=Competence(name="")
        competence.name=' '.join(fake.words()).title()
        records+=f'{k+1}. {competence.name} <br/>'
        competence.save()
    return HttpResponse(f"<h2>{totalrecord} Successful created</h2> {records}  ")

def fakeBundle(request,totalrecord):
    fake=Faker()
    records=""
    for k in range(totalrecord):
        bundle=Bundle(name="")
        bundle.name=' '.join(fake.words()).title()
        records+=f'{k+1}. {bundle.name} <br/>'
        bundle.save()
    return HttpResponse(f"<h2>{totalrecord} Successful created</h2> {records}  ")


def fakeQualities(request,totalrecord):
    fake=Faker()
    import random
    result=""
    competences=Competence.objects.all()
    
    for _ in range(totalrecord):
        competence=random.choice(competences)
        quality=Quality.objects.create(name=fake.sentence(),competence=competence)
        result+=f'{quality.name}<br/>'
    # return HttpResponse(f"<h2>{totalrecord} Successful created <br/> {quality} <h2> ")
    return HttpResponse(f"<h2>{totalrecord} Successful created </h2> <br/> {result} ")

def fakeQualities2(request,totalrecord):
    fake=Faker()
    competences=Competence.objects.all()
    result=""
    totalcreated=0
    for competence in competences:
        count=0
        result+=f"<br/> <h5> {competence}</h5> "
        for _ in range(totalrecord):
            count+=1
            quality=Quality.objects.create(name=fake.sentence(),competence=competence)
            result+=f'{count}. {quality.name}<br/>'
        totalcreated+=totalrecord
    return HttpResponse(f"{totalcreated} Successful created  {result}   ")

def fakeBundleCompetence(request,totalrecord):
    fake=Faker()
    bundles=Bundle.objects.all()
    comps=Competence.objects.all()
    result=""
    totalcreated=0
    for bundle in bundles:
        count=0
        result+=f"<br/> <h5> {bundle}</h5> "
        
        for _ in range(totalrecord):
            count+=1
            randComp=random.choice(comps)
            bundle.competences.add(randComp) # add a random competence to bundle
            result+=f'{count}. {randComp.name}<br/>'
        totalcreated+=totalrecord
    return HttpResponse(f"{totalcreated} Successful created  {result}   ")
    
