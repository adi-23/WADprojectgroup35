from django.db import models
from django.contrib.auth.models import AbstractUser

#Abstract user is the module in django for creating multiple users in the appication

class User(AbstractUser): #CHEKING THE Whether user is serviceuser or serviceprovider
    is_serviceuser = models.BooleanField(default=False)
    is_serviceprovider = models.BooleanField(default=False)

class serviceuser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True) #Serviceuser is mapped one-to one field to Abstract User 
    Email = models.EmailField(max_length=254)

class serviceprovider(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)#Serviceprovider is mapped one-to one field to Abstract User 
    
    def __str__(self):
        return str(self.user)#returns this service[prviderobject
