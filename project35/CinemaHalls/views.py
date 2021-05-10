from django.shortcuts import render,redirect
from hotels.models import Place
from .models import CinemaHall
from .form import CinemaHallForm
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from authentication.models import serviceprovider,User
from .filters import CinemaHallFilter
from django.http import HttpResponse
<<<<<<< HEAD
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #
from django.views.generic import (
    DetailView,
                                #Used class based generic views for detais and updating the information of service provider

    UpdateView,
    
=======
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ( # Used class based generic views for details and updating the information
    DetailView,
    UpdateView,
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd
)




def form_view(request,user_id):
    
<<<<<<< HEAD
    if request.method == "POST": #the data sent through the form using request.POST method
        form=CinemaHallForm(request.POST,request.FILES)  
        k=0
        places=Place.objects.all()
                                #if the serviceprovider specified place is not in the data base added it to the table
        for place in places:
            if form['cinemahall_place'].value() == place.place_name:   
=======
    if request.method == "POST": #If method is POST the data sent through form
        form=CinemaHallForm(request.POST,request.FILES)
        k=0
        places=Place.objects.all()
        for place in places: # If the serviceprovider specified place is not in the database, Add it to the table 
            if form['cinemahall_place'].value() == place.place_name:
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd
                k=1
                obj=place
                break
        if k == 0:
            obj=Place(place_name=form['cinemahall_place'].value())
            obj.save()
<<<<<<< HEAD
                                             #storing and saving cinemahall details in the database
        user=User.objects.get(id=user_id)    #searching user information baseed on user_id
        cinemaObj=CinemaHall(theatre_owner=user,current_movie=form['current_movie'].value(),cinemahall_name=form['cinemahall_name'].value(),seats=form['seats'].value(),timing=form['timing'].value(),cinemahall_address=form['cinemahall_address'].value(),cinemahall_place=obj,cinemahall_contactinfo=form['cinemahall_contactinfo'].value(),cinemahall_image=form['cinemahall_image'].value())
        cinemaObj.save()
                
        return render(request,'hotels/redir.html')
    else:
        #if serviceprovider already added cinemahall details then render the information of cinemhall based on user_id other wise render cinemahall form 
        if (CinemaHall.objects.filter(theatre_owner_id=user_id).first()) is not None:
            temp =CinemaHall.objects.filter(theatre_owner_id=user_id).first() #looking for information of cinemahall
=======
        # Storing and saving the cinema hall details in the database
        user=User.objects.get(id=user_id) # Searching the user information based on user id
        cinemaObj=CinemaHall(theatre_owner=user,current_movie=form['current_movie'].value(),cinemahall_name=form['cinemahall_name'].value(),seats=form['seats'].value(),timing=form['timing'].value(),cinemahall_address=form['cinemahall_address'].value(),cinemahall_place=obj,cinemahall_contactinfo=form['cinemahall_contactinfo'].value(),cinemahall_image=form['cinemahall_image'].value())
        cinemaObj.save()
                
        return render(request,'authentication/Serviceuserhomepage.html')
    else: # If the serviceprovider has already added cinema hall details then get the detailed information of their cinema hall otherwise render the cinema hall form 
        if (CinemaHall.objects.filter(theatre_owner_id=user_id).first()) is not None:
            temp =CinemaHall.objects.filter(theatre_owner_id=user_id).first() # Looking for information of their cinema hall
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd
            i=temp.id
            url = '/cinemahalls/cinemahall/{}/'.format(i)
            return redirect(url)

        else:
            form= CinemaHallForm()
            return render(request,'CinemaHalls/cinemahall_form.html',{'form':form})

<<<<<<< HEAD
class CinemaHallDetailView(DetailView): # with help of detail view we get detail information of cinemahall 
    model=CinemaHall


class CinemaHallUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):      #using update view updating cinemahall details
    model=CinemaHall
    fields=['cinemahall_name','cinemahall_image','seats','cinemahall_address','cinemahall_place','cinemahall_contactinfo','timing','current_movie']

    def form_valid(self, form):         #if person is serviceprovider then he/she can edit the form instance
        if self.request.user.is_serviceprovider :
            form.instance.theatre_owner = self.request.user #storing user details in the form
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the Cinemahalls') #Only serviceprovider can edit the form but users can't
=======
class CinemaHallDetailView(DetailView): # With the help of DetailView, we can get detailed information of each cinema hall
    model=CinemaHall


class CinemaHallUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Using UpdateView, we are updating the cinema hall details
    model=CinemaHall
    fields=['cinemahall_name','cinemahall_image','seats','cinemahall_address','cinemahall_place','cinemahall_contactinfo','timing','current_movie']

    def form_valid(self, form): # Here, if a person is serviceprovider then he/she can edit the form instance
        if self.request.user.is_serviceprovider :
            form.instance.theatre_owner = self.request.user # Storing the user details in the form
            return super().form_valid(form)
        else :
            return HttpResponse('Users cannot insert the Cinemahalls') # Only serviceprovider can edit the form, users can't edit it.
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd

    def test_func(self):    
        cinemahall =self.get_object()
<<<<<<< HEAD
        if self.request.user == cinemahall.theatre_owner: #checking whether the current login user is the owner of cinemahall 
=======
        if self.request.user == cinemahall.theatre_owner: # Checking whether the current login user is the owner of the cinema hall
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd
            return True
        return False


def cinemahalls(request):

    return render(request,"CinemaHalls/cinemahalls.html",{
    'Place':Place.objects.all()
    })

<<<<<<< HEAD

def select(request):                #searching respective cinemahall details in a specified location
    result=request.GET['places'] #specified locaton
    iid=0
    for place in Place.objects.all():  #searching the id of specificed location in data base
        if place.place_name==result: #if exists store it in iid
=======
# Searching respective cinemahalls details in a specified location
def select(request):
    result=request.GET['places'] # specified location
    iid=0
    for place in Place.objects.all(): # Searching the id of specified location in the database
        if place.place_name==result:
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd

            iid=place.id
            break

<<<<<<< HEAD
    cinemahalls_info= CinemaHall.objects.filter(cinemahall_place=iid) #filter in cinemahall acording to the place
    context={'cinemahallsinfo': cinemahalls_info, }
    return render(request,"CinemaHalls/cinemahalls.html",{ #rendering the detais in user specified place
=======
    cinemahalls_info= CinemaHall.objects.filter(cinemahall_place=iid) # Filtering the cinemahalls according to the place
    context={'cinemahallsinfo': cinemahalls_info, }
    return render(request,"CinemaHalls/cinemahalls.html",{ # Rendering the cinema hall details in the user specified location
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd
    'Place': Place.objects.all(),
    'CinemaHalls':cinemahalls_info,
    'place_id': iid #sending to filter for place

    })


<<<<<<< HEAD

def CinemaHallListview(request,place_id): #filtering the cinemahall name based on current movie
=======
# Filtering and getting the cinema hall names based on doctors information
def CinemaHallListview(request,place_id):
    # model=Hotel
    # template_name='hotels/hotel_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = HotelFilter(self.request.GET, queryset=self.get_queryset())
    #     return context
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd
    
    place=Place.objects.get(id=place_id)
    theatre_list=CinemaHall.objects.filter(cinemahall_place=place)
    h = CinemaHallFilter(request.GET,queryset=theatre_list)

    return render(request,'cinemahalls/cinemahalls_list.html',{'filter': h,'cinemahall': theatre_list})



# About our Website
def aboutus(request):
    return render(request,"Visitplace/AboutUs.html")

# Information about website owners
def contact(request):
    return render(request,"Visitplace/Contact.html")


def homepage(request):
    return render(request,'authentication/Serviceuserhomepage.html')