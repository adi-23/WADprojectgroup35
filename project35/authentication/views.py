from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .form import ServiceProviderSignUpForm, ServiceUserSignUpForm


class serviceuser_register(CreateView): #Saving the user in database by creating User from the form detais
    model = User 
    form_class = ServiceUserSignUpForm #initiating form
    template_name = "authentication/serviceuser_register.html"

    def form_valid(self, form):
        user = form.save() #Saving if form is valid
        
        return redirect('/')


class serviceprovider_register(CreateView): #Saving the user in database by creating User from the form detais
    model = User
    form_class = ServiceProviderSignUpForm #initiating form
    
    template_name = "authentication/serviceprovider_register.html"

    def form_valid(self, form):
        user = form.save()#Saving if form is valid
       
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        #if method is POST the data sent through form
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #user is authenticated
            if user is not None :
                login(request,user)
                if user.is_serviceprovider:
                        return redirect('../serviceproviderhome/')
                else:
                    return redirect('../userhome/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'authentication/login.html',
    context={'form':AuthenticationForm()})


def serviceproviderhome(request): #to render service provider homepage
    return render(request,'authentication/userHomepage.html',context={'user': request.user})

def userhome(request): # render serviceuser home page
    return render(request,'authentication/Serviceuserhomepage.html',context={'username': request.user.username})
# view for logout (if user clicks logout redirects to homepage)
def logout_view(request):
    logout(request)
    return redirect('/')

#this renders homepage page to get login and register buttons
def home(request):
     render(request,'travel/home.html')

def serviceproviderhome(request):
    return render(request,'authentication/userHomepage.html',context={'user': request.user})

<<<<<<< HEAD
=======
def userhome(request):
    return render(request,'authentication/Serviceuserhomepage.html',context={'username': request.user.username})
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd
