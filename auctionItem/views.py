from django.shortcuts import render,get_object_or_404
from auctionItem.models import Lot,Category,Auction,Seller
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
import redis
from django.conf import settings
from django.utils.safestring import mark_safe
import json
# connect to redis



# Create your views here.

def all_item(request,category_slug=None):
    products=Lot.objects.filter(is_trending=True)
    category=None
    categories=Category.objects.all()
    
    print(category_slug)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    print(category)
    
    items_trending = Lot.objects.filter(is_trending=True)
    paginator =Paginator(items_trending, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    context={
        'items':page_obj,
        'products':products,
        'categories':categories,
        'category':category, 
        
    }
    return render(request,'all_item.html',context)


def single_item(request,item_id,slug):
    lot=get_object_or_404(Lot,
                          id=item_id,
                          slug=slug,
                          )
    auction= get_object_or_404(
        Auction,id=item_id
    )
    
    print(auction)
    ####SEller ka page banao
    
    
   
    
    room=False
    if request.user.is_authenticated:
        
        room= request.user
        print(room)
    slugged=Lot.objects.filter(slug=slug)
    category=get_object_or_404(Category,slug=slug) 
    
    
    context={
        'room_name_json':mark_safe(json.dumps(item_id)),
        'auctionid':auction.id,
        'username':mark_safe(json.dumps(request.user.username)),
        'lot':lot,
        'slugged':slugged,
        'category':category,
        'room':room,
        'endingtime': auction.curr_time,
        'total_views':5,
    }
    return render(request,'single_item.html',context)


def search(request,category_slug=None):
    filter_category=Lot.objects.all()
    
    
    
    if 'search_box' in request.GET:
        search_box=request.GET['search_box']
        if search_box:
            filter_category=filter_category.filter(
                                                    Q(product_name__icontains=search_box)|
                                                    Q(description__icontains=search_box)|            
                                                     Q(category__name__icontains=search_box)|
                                                    Q(seller__name=search_box)).distinct()
            
            
                                                   
    category=None 
    categories=Category.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)   
        filter_category = filter_category.filter(category=category)
    filter_category = list(filter_category)
    live_items = []
    upcoming_items = []
    for item in  filter_category:
        if item.auction_status == "live":
            live_items.append(item)
        elif item.auction_status == "upcoming":
            upcoming_items.append(item)
    live_items.sort(key=Lot.time_to_end, reverse=True)
    upcoming_items.sort(key=Lot.time_to_start, reverse=True)
    filter_category = live_items + upcoming_items    
     
    lots=Lot.objects.order_by('-year_published')
    paginator = Paginator(lots, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    
    context={
        'lots' :page_obj,
        'items':Lot.objects.all(),
        'filters':filter_category,
        'category':category,
        'categories':categories,
        
    }
    return render(request,'search.html',context)


def seller_page(request,seller):
    
    seller=Seller.objects.get(id=seller)
    lots=Lot.objects.all()
    
    
    #print(lot.filter(seller=seller[0]))
    return render(request,'seller-page.html' ,{ 'lot':lots,'seller':seller } )
    

# @login_required
# def chat_room(request, item_id):
#     try:
#         # retrieve course with given id joined by the current user
#         course = request.user.get(id=item_id)
        
#     except:
#         # user is not a student of the course or course does not exist
#         return HttpResponseForbidden()
#     return render(request, 'single-page.html', {'course': course})



