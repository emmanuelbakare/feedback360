from django.db import models
from competence.models import Competence
from datetime import datetime
from utils.models import BaseModel


class QualityManager(models.Manager):
    def get_competence(self):
        return super().get_queryset().competence
    
    def active(self):
        return super().get_queryset().filter(active=True)
        
    
# Create your models here.
class Quality(BaseModel):
    name=models.CharField(max_length=250)
    competence=models.ForeignKey(Competence, on_delete=models.CASCADE, related_name='qualities')
    active=models.BooleanField(default=True)
    
    objects=QualityManager()
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering=['created']
        verbose_name_plural='qualities'