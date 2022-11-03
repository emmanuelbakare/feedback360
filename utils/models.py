from django.db import models
from django.apps import apps
from django.db.models import query

class BaseModel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


# def add_action(actions=):
#     return actions

class ModelFields:
    ''' get a model Class and return all the fields it contains
        e.g. get_model_fields(Model_Obj)
        show =  if you want to only return specific fields, specify the fields in the show list parameter
            e.g. get_model_fields(Model_Obj, show=['name', 'description]
        hide = if you want to exclude any field from the result specify it in the exclude parameter
            e.g. get_model_fields(Model_Obj, hide=['id'])
    '''
    def __init__(self, model,sno=True):
        self.fields=self.get_all_fields(model)
        self.sno=sno




    def get_all_fields(self,model):
        if isinstance(model, query.QuerySet):
            model=model.first()
            if not model: # if there are no records in the queryset then return an empty list
                real_fields={}
                # context={"sno": self.sno, "fields":real_fields}
                return real_fields

        
        # get fields from model
        fields_=model._meta.get_fields()
        all_fields={field.name:field.__class__.__name__ for field in fields_ if isinstance(field, models.fields.Field)}
        print('ALL FIELDS', all_fields)
        return all_fields

    def all(self):
        context={"sno": self.sno, "fields":self.fields}
        return context

    def show(self,fields=[]):
        if fields:  # return only fields specified in show list param
            # real_fields=[new_field for new_field in show if new_field in real_fields]
            real_fields={}
            real_fields={key:self.fields[key] for key in self.fields and fields}
            context={"sno": self.sno, "fields":real_fields}
            return context
    
    def hide(self, fields=[]):
        if fields: # remove the fields specified in hide list param
            real_fields={}
            for field in fields:
                if field in self.fields:
                    new_fields=self.fields.copy()  # copy the field to another var so that the resultant pop will not affect self.fields
                    new_fields.pop(field)
            

            # real_fields={key:self.fields[key] for key in self.fields and fields}
            context={"sno": self.sno, "fields":new_fields}
            return context



def get_model_fields(cls, show=[], hide=[], sno=True):
    ''' get a model Class and return all the fields it contains
        e.g. get_model_fields(Model_Obj)
        show =  if you want to only return specific fields, specify the fields in the show list parameter
            e.g. get_model_fields(Model_Obj, show=['name', 'description]
        hide = if you want to exclude any field from the result specify it in the exclude parameter
            e.g. get_model_fields(Model_Obj, hide=['id'])
    '''

    context={}

    if isinstance(cls, query.QuerySet):
        cls=cls.first()
        if not cls: # if there are no records in the queryset then return an empty list
            # real_fields=[]
            real_fields={}
            context={"sno": sno, "fields":real_fields}
            return context

    
    # get fields from model
    fields=cls._meta.get_fields()
    # real_fields=[field.name for field in fields if isinstance(field, models.fields.Field)]
    real_fields={field.name:field.__class__.__name__ for field in fields if isinstance(field, models.fields.Field)}



    if show:  # return only fields specified in show list param
        # real_fields=[new_field for new_field in show if new_field in real_fields]
        real_fields={new_field:new_field.__class__.__name__ for new_field in show if new_field in real_fields}
        # new_fields=real_fields.intersection(show)
        
    if hide: # remove the fields specified in hide list param
        # real_fields=[new_field for new_field in real_fields if new_field not in hide]
        real_fields={new_field:new_field.__class__.__name__ for new_field in real_fields if new_field not in hide}
        # new_fields=real_fields.difference(hide)
   

    context={"sno": sno, "fields":real_fields}
    return context # return all the fields if hide or show is not specified


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








    
   