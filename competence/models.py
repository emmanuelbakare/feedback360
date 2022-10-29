from django.db import models
from utils.models import BaseModel
from datetime import datetime
from accounts.models import Person

# Create your models here.

class Bundle(BaseModel):
    name=models.CharField(max_length=250)
    assessment=models.ManyToManyField(Person, through='Assessment',
                                      through_fields=('bundle','assessed'))
    def __str__(self):
        return self.name
    
    def addCompetence(self, comp ):
        self.competences.add(comp)
        return self
class Competence(BaseModel):
    name=models.CharField(max_length=250)
    bundles=models.ManyToManyField(Bundle, related_name='competences')
    # bundles=models.ManyToManyField(Bundle)
   
    
    def __str__(self) -> str:
        return self.name





#this contain a group of bundles assigned to someone who is to be assessed.   
from datetime import datetime
class Assessment(BaseModel):
    assessed = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="assessments")   
    assessor = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name="attached_assessments")   
    bundle  = models.ForeignKey(Bundle, on_delete=models.CASCADE, related_name="assessed_bundle") 
    # assessor = models.IntegerField(blank=True,null=True)   
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=True)
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'{self.assessed.first_name} {self.assessed.last_name}({self.bundle.name})'

    class Meta:
        ordering=['-id']
        unique_together=[['assessed','bundle','start_date']]
    