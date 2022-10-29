from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class PersonUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValidationError("You must enter email address")
        if not first_name:
            raise ValidationError("You must enter first name")
        if not last_name:
            raise ValidationError("You must enter Last name")
        
        user=self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email, first_name, last_name, password=None):
        user=self.create_user(email=email, first_name=first_name, last_name=last_name,password=password)
        user.is_staff=True
        user.is_superuser=True
        user.is_admin=True
        user.save(using=self._db)
        return user

    
class Person(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=50, unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    is_assessor=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    username=None 
    
    objects=PersonUserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name']
    def __str__(self) -> str:
        return self.email 
    
    def has_perm(self, perm, obj=None):
        return True 
    
    def has_module_perms(self, app_label):
        return True
    
    # def save(self,*args, **kwargs):
    #     if not self.profile:
    #         super().save(*args, **kwargs)
    #         print('New Person created', self)
    #         profile=Profile.objects.create(Person=self)
    #         print('PERSON PROFILE',profile )
    #     print('CAME HERE')

 

class Profile(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile',default='default.jpg')
    gender=models.CharField(max_length=10)
    profession=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    dob=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.person.email} profile'
    

    
