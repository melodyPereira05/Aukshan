from django.contrib import admin
from auctionItem.models import Lot,Seller,Category,Auction,Message,Wishlist,Contact,Subscribe
# Register your models here.
admin.site.register(Lot)  
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Auction)
admin.site.register(Message)
admin.site.register(Wishlist)
admin.site.register(Contact)
admin.site.register(Subscribe)