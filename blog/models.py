from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

    
class PublishedManager(models.Manager):
    
    def get_queryset(self):
        
        return super(PublishedManager,
                   self).get_queryset().filter(status='published')
       


class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published')
    )
    
    title=models.CharField(max_length=300)
    slug=models.SlugField(max_length=300,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=models.Manager()
    published=PublishedManager()
    
    tags=TaggableManager()  #it allows to add,retrive and remove tags from post.
    
    class Meta:
        ordering=('-publish',)  
        #ERRORS:
        #blog.Post: (models.E014) 'ordering' must be a tuple or list (even if you want to order by only one field).
    
    def get_absolute_url(self):
        return reverse('blog-app:post-detail', 
                       args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug]
                       )
    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    class Meta:
        ordering=('created',)
        
    def __str__(self):
        return f" Comments by {self.name} on {self.post}"
            
            
    
