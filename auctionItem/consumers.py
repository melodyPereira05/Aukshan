import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
from auctionItem.models import Message,Auction,Lot
from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404
from datetime import timedelta

User=get_user_model()





class ChatConsumer(WebsocketConsumer):
    
    def fetch_messages(self,data):
        print(int(data['auction_id']))
        auction = Auction.objects.get(id=int(data['auction_id']))
        messages = Message.objects.filter(auction=auction)
        print(auction)
        
        print(messages)
           
        
        content={
            'command':'messages',
            'messages': self.messages_to_json(messages),
            
        }
        
        self.send_message(content)
        
    def new_message(self,data):
        author=data['from']
        print(int(data['auction_id']))
        auction = Auction.objects.get(id=int(data['auction_id']))
        author_user=User.objects.filter(username=author)[0]
        message=Message.objects.create(author=author_user, price=data['message'],auction=auction)
        message.save()
        #print(messages)

        content={
            #'id':message.author.id,
            'command':'new_message',
            'message':self.message_to_json(message),
        }
        
        return self.send_chat_message(content)
        
       
        
    def messages_to_json(self,messages):
        result=[]
        for message in messages:
            result.append(self.message_to_json(message))
        return result
        
    def message_to_json(self,message):
        return{
            'id':message.author.id,
            'author':message.author.username,
            'price':message.price,
            'timecap':str((message.timecap +timedelta(hours=5.5)).strftime('%H:%M')),  #django time differnce is 5.5hrs
        }
        
        
    commands={
        'fetch_messages':fetch_messages,
        'new_message':new_message,
    }
    
    def connect(self):
        
        # accept connection
        
        self.user = self.scope['user']
        #print(self.user)
        self.id = self.scope['url_route']['kwargs']['item_id']
        #self.slug = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = 'auction_%s' % self.id 
        #print(self.room_group_name)
        # join room group
        async_to_sync(self.channel_layer.group_add)(
        self.room_group_name,
        self.channel_name
        )
        self.accept()
        
        
    def disconnect(self, close_code):
        # leave room group
        async_to_sync(self.channel_layer.group_discard)(
        self.room_group_name,
        self.channel_name
        )
    
    
    
    # receive message from WebSocket,add messages as well in db
    def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        if data['command'] in self.commands:
            self.commands[data['command']](self,data)
        
       
        
    def send_chat_message(self,message):
        
       
        # send message to WebSocket
        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
        {
        'type': 'chat_message',
        'message': message,
        #'user': self.user.username,
        #'datetime': now.isoformat(),

        }
        )
        
    # receive message from room group
    def chat_message(self, event):
        message=event['message']
        
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))
        
    def send_message(self,message):
        self.send(text_data=json.dumps(message))
         
        
        