from django.apps import apps
from django.db import models
from utils.models import MakeModelOrQueryset



    

class EndPoints:
    '''generate a dictionary of endpoint (urls) and database queryset that will be attached to a template as context data'''
    def __init__(self, model_name, app_name=None, request=None, defaults=False, pk=None):
        
        ''' if model_name is a model object then store it in self.obj2 
            if model_name is a queryset, store it in self.object_list
            if model_name is a str then get self.obj2 and self.object_list MakeModelOrQueryset to get the mode or queryset'''
        if isinstance(model_name,models.Model):
            self.obj2 = model_name
            self.name= model_name.__class__.__name__.lower()
            # self.name= model_name.__class__.__name__.lower() if model_name.first() else ''
            
        
        elif isinstance(model_name, models.query.QuerySet):
            self.object_list=model_name
            self.name=model_name.first().__class__.__name__.lower() if model_name.first() else '***'

        elif isinstance(model_name, str):
            self.name=model_name
            if pk:
                self.obj2 = MakeModelOrQueryset(model_name,app_name, pk=pk).queryset
            else:
                print('ABOUT TO MAKE QUERYSET WITH MakeModelOrQueryset')
                self.object_list = MakeModelOrQueryset(model_name,app_name).queryset



        if defaults:
            self.defaults()
    
    def new_path(self, key, value):
        ''' a method to set attributes on all endpoint instance 
        use:  action('age', 34) will set attributes age to 34 on an EndPoint instance'''
        if self.__dict__.get(key):
            self.__dict__[key] = value
        else:
            setattr(self,key,value)
        
        return self

    def remove_path(self,key):
        ''' delete an existing dictionary item'''
        if self.__dict__.get(key):
            del self.__dict__[key]
        return self     


    def defaults(self):
        ''' return sets of urls paths that is most likely  to be used to generate endpoints
        this include the create, retreive, update and delete urls '''
        print('...add default paths')
        self.__dict__['create']=f'{self.name}:create'
        self.__dict__['retrieve']=f'{self.name}:retrieve'
        self.__dict__['update']=f'{self.name}:update'
        self.__dict__['delete']=f'{self.name}:delete'

        return self
    
        
    @property 
    def query_object(self):
        ''' returns the Model object. Either a queryset or a model object instance. 
        If there is no queryset or model instance then return None'''
        if hasattr(self,'object_list'):
            return self.object_list
        elif hasattr(self,'obj2'):
            return self.obj2
        else:
            return None
        
    @property 
    def model_object(self):
        if hasattr(self,'obj2'):
            return self.obj2
        return None


    @property
    def context(self):
        ''' return a dictionary of the endpoints generated from the instance dunder __dict__  method'''
        return self.__dict__.copy()
    

    

    # def get_model(self, model_name, app_name=None, pk={}):
    #     ''' Build a queryset from only the model name
    #      model name is entered as a string 'model_name' 

    #      use:
    #         get_model(model_name, app_name)
         
    #      argument:
    #         model_name:str|queryset: a queryset instance or name of the model-system generates the QuerySet
    #         app_name: the app name  (created with manage.py startapp app_name)
        
    #      returns:
    #         queryset
    #         '''
    #     #if model_name is a queryset return it if not build the queryset from the model_name 
       
    #     if isinstance(model_name, models.query.QuerySet):
    #         return model_name
        
    #     # if the app_name is same name as the model_name or app_name is not inputed    
    #     model_name=model_name.lower()
    #     if app_name is None or len(app_name)==0:
    #         model_base=apps.get_model(model_name, model_name)
    #     else:
    #         model_base=apps.get_model(app_name,model_name)
        

        
           
    #     # return self._get_model_obj_or_queryset(model_base,pk)
    #     return model_base.objects.all()
    



# endpoint=EndPoints("competence",pk=20, defaults=True)
# print('ENDPOINT OBJECT \n', endpoint)
# # endpoint.defaults()
# endpoint.new_path('gender','male')
# context=endpoint.context
# print('ENDPOINT CONTEXT: \n',context)

# print('NEW QUERY \n',MakeModelOrQueryset("competence", pk=2).queryset ) 

# print('ENDPOINT QUERY OBJECT ', endpoint.query_object)
      