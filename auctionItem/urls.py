from django.urls import path
from  . import views

app_name='auction'
urlpatterns = [

     
    path('',views.all_item, name="all-item"),
    path('search/',views.search, name="search-page"),
    path('<slug:category_slug>/',views.all_item, name="items_by_category"),
    path('search/<slug:category_slug>/',views.search, name="items_by_category"),
    path('<int:item_id>/<slug:slug>/',views.single_item, name="single-item"),
   
    
    
    
    
    
]