from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required

from accounts.forms import RegisterForm,LoginForm
from django.contrib.auth import get_user_model, views as auth_view


# Create your views here.
# @login_required
def home(request):
    return render(request,'accounts/home.html',{})
    
# @login_required
def profile(request):
    # user=get_user_model().objects.get(pk=pk)
    # user=
    if request.FILES:
        photo=request.FILES['photo']
        request.user.profile.image.save(photo.name,photo)
        
    context={'user':request.user}
    return render(request,'accounts/profile.html',context)

def register(request):
    form=RegisterForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('accounts:profile')
    context={
        'form':form,
        'title':'Register Form 1'
        }
    return render(request,'accounts/register.html',context)

def login2(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile', pk=request.user.pk)
    form=LoginForm(request.POST or None)
    if request.method=="POST":
         email=request.POST.get('email')
         password=request.POST.get('password')
         
         if form.is_valid():
            user=authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:profile', pk=user.pk)
            
    context={'form':form}
    return render(request, 'accounts/login.html', context)

def logout2(request):
    logout(request)
    return redirect('accounts:login2')

class CustomLoginView(auth_view.LoginView):
    template_name='accounts/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('accounts.profile')
   
        # return reverse_lazy('accounts:profile',kwargs={'pk':self.get_form.cleand_data.get('pk')})
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print('LOGINVIEW \n',dir(self))
        
        # for field in fields:
        #     field=fields[field]
        #     print(field)
        #     field.help_text="Something here"
        #     field.widget.attrs.update({'class':'form-control'})
        # print(dir(field))
        # print(dir(field.widget))
        
    # form=self.get_form_class()

# class Register(generic.FormView):
#     template_name='accounts/register.html'
#     form_class=RegisterForm
#     success_url='/accounts/profile/'
    
#     def form_valid(self,form):
#         return self().form_valid(form)
#     # def get_context_data(self,**kwargs):
#     #     context=super().get_context_data(**kwargs)
#     #     context['title']='Register Form 2'
#     def post(self, request):
#         form=self.form_class(request.POST)
        
#         if form.is_valid():
#             print(form)
#             form.save()
            
        
# class Register2(View):
#     template_name='accounts/register.html'
#     form_class=RegisterForm 
#     success_url='/accounts/profile/'


def uploadphoto(request):
    file=request.FILES["photo"]
    print(file)
    print(dir(file))
    return HttpResponse(f"{file}")