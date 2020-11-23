from django.urls import path
from  . import views


urlpatterns = [
    
    path('', views.index , name="home-page"),
    path('about/',views.about, name="about-page"),
    path('contact-us/',views.contact_us,name="contact-us")
    
    
    
]