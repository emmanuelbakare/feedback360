from django import forms 
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    
    class Meta:
        model=get_user_model()
        fields=['email','first_name','last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        fields=self.fields
        for field in fields:
            fields[field].help_text=''
            fields[field].widget.attrs.update({'class':'form-control'})
        # print(dir(self.fields[field].widget.attrs))
        # print('GOT TO REGISTER FORM')

# class LoginForm(forms.Form):
class LoginForm(AuthenticationForm):
    # email=forms.CharField(max_length=100)
    # password=forms.CharField(widget=forms.PasswordInput, max_length=100)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        fields=self.fields
        for field in fields:
            fields[field].widget.attrs.update({'class':'form-control'})
    
              