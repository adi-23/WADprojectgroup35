from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.home,name="home"),
    path('serviceuser_register/',views.serviceuser_register.as_view(),name="serviceuser_register"),#url for registration of serviceuser
    path('serviceprovider_register/',views.serviceprovider_register.as_view(),name="serviceprovider_register"),#url for registration of serviceprovider
<<<<<<< HEAD
    path('serviceproviderhome/',views.serviceproviderhome,name="serviceproviderhome"),#url to render serviceprovide homepage
    path('userhome/',views.userhome,name="userhome"),#url to render serviceuserhome page
    path('login/',views.login_request,name="login"),#For login
    path('logout/',views.logout_view,name="logout")#for logout
=======
    path('login/',views.login_request,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('serviceproviderhome/',views.serviceproviderhome,name="serviceproviderhome"),
    path('userhome/',views.userhome,name="userhome"),
>>>>>>> dfe14b04a151ae47cef7697ca4afba252bc3e6cd


]
