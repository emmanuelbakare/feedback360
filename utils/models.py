from django.db import models
from django.apps import apps
from django.db.models import query

class BaseModel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class MakeQueryset:
    ''' generate a queryset from a model string name and app name
    if app_name is not supplied use the model name as app name '''
    
    def __init__(self, model_name,app_name=None):
        self._queryset=self.get_queryset(model_name, model_name)
        
    
    @property
    def queryset(self):
        return self._queryset

    def get_queryset(self, model_name,app_name=None):
        
        if app_name is None or len(app_name)==0:
            model_base=apps.get_model(model_name, model_name)
        else:
            model_base=apps.get_model(app_name,model_name)
        return model_base.objects.all()
  
    
class MakeModelOrQueryset:
    ''' Build a queryset or an model object (if pk is supplied)'''
    def __init__(self,model_name,app_name=None, pk=None):
        self.model=self.get_model_query(model_name,app_name,pk)
    

    def get_model_query(self,model_name, app_name, pk):
        ''' use the string model_name to generate either a queryset or an model object if pk is supplied'''
        print(f"model_name: {model_name}, app_name:{app_name}, pk:{pk}")
        if isinstance(model_name, query.QuerySet):
            return model_name
        
        if app_name is None or len(app_name)==0:
            model_base=apps.get_model(model_name, model_name)
        else:
            model_base=apps.get_model(app_name,model_name)
        if pk:
            return self.get_model_obj(model_base,pk)
        else:
            return self.get_queryset(model_base)


        
    def get_queryset(self, model_base):
        ''' generate a queryset from a model instance run this method if no pk is provided'''
        return model_base.objects.all()

    def get_model_obj(self, model_base, pk):
        ''' generate model instance using the provided pk'''
        try:
            return model_base.objects.get(pk=pk)
        except model_base.DoesNotExist:
            return None

    @property 
    def queryset(self):
        ''' return the model (queryset or model object) created with either  get_queryset() or get_model_obj()'''
        return self.model 

# mod=MakeModelObjectOrQueryset("competence")
# print('MakeModelObjectOrQueryset :', mod) 
# print('MakeModelOBjectOrQueryset model :', mod.queryset) 








    
   