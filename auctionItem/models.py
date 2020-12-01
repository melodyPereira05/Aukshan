from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class Category(models.Model):
    name=models.CharField(unique=True,max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,unique=True)
    
    def get_absolute_url(self):
        return reverse('auction:items_by_category',args=[self.slug])
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    
    def __str__(self):
        return self.name 

class Seller(models.Model):
    name=models.CharField(max_length=200)
    seller_photo=models.ImageField(upload_to='photos/seller/%Y/%m/%d/')
    contact_no =models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    def get_absolute_url(self):
        return reverse('auction:seller-page',args=[self.id])
    
    def __str__(self):
        return self.name
    
class Lot(models.Model):
    category=models.ForeignKey(Category, related_name='lots', on_delete=models.CASCADE)
    seller =models.ForeignKey(Seller,on_delete=models.DO_NOTHING)
    slug=models.SlugField(max_length=200,db_index=True)
    product_name=models.CharField(max_length=200,db_index=True)
    is_live=models.BooleanField(default=False)
    base_price=models.IntegerField(default=0.0)
    current_price=models.IntegerField(default=0.0)
    description=models.CharField(max_length=500)
    main_photo=models.ImageField(upload_to='photos/main/%Y/%m/%d/')
    photo1=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo2=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo3=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    photo4=models.ImageField(upload_to='photos/optional/%Y/%m/%d/',blank=True)
    is_trending=models.BooleanField(default=False)
    on_banner=models.BooleanField(default=False)
    year_published=models.DateTimeField(default=datetime.now())
    #  tags:one to many fields 
    
    def get_absolute_url(self):
        return reverse('auction:single-item',args=[self.id,self.slug])
    
    
    
    
    class Meta:
        ordering=('product_name',)
        index_together=(('id','slug'),)
    
    
    def __str__(self):
        return self.product_name
    
  
class Wishlist(models.Model):
    lot=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,db_index=True,null=True,blank=True)
    lot_id=models.IntegerField()
    Wishlisted_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=False)
    
    def get_absolute_url(self):
        return reverse('auction:single-item',args=[self.lot_id,self.slug])
    def __srt__(self):
        return self.name

class Contact(models.Model):
    lot=models.CharField(max_length=1000)
    lot_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,db_index=True,null=True,blank=True)
    message=models.TextField(blank=True)
    contact_date=models.DateTimeField(default=datetime.now,blank=True)
    user_id=models.IntegerField(blank=True)
    
    def get_absolute_url(self):
        return reverse('auction:single-item',args=[self.lot_id,self.slug])
    
    
    
    def __str__(self):
        return self.name
    
    
  
class Auction(models.Model):
    start =  models.DateTimeField(auto_now=False)
    curr_time =  models.DateTimeField(auto_now=False)
    item = models.OneToOneField(
    Lot, on_delete=models.CASCADE, related_name="auction")
    
    
    def __str__(self):
        return self.item.product_name



class Message(models.Model):
    auction=models.ForeignKey(Auction, on_delete=models.CASCADE,related_name='auction') 
    author=models.ForeignKey(User,related_name='author_messsages',on_delete=models.CASCADE)
    timecap = models.DateTimeField(auto_now_add=True)
    price = models.TextField()
   
    
    

    def __str__(self):
        return self.author.username
    
    
    
class Subscribe(models.Model):
    email=models.EmailField()
    
    def __str__(self):
        return self.email
  
        
