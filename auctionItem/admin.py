from django.contrib import admin
from auctionItem.models import Lot,Seller,Category,Auction,Message
# Register your models here.
admin.site.register(Lot)  
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Auction)
admin.site.register(Message)