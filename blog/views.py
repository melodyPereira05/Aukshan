from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  #Emptypage and pagennotinteger bot yet updated
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

# Create your views here.

def post_list(request,tag_slug=None):
    posts=Post.published.all()
    common_tags=Post.tags.most_common()
    tag=None
    if tag_slug:
       
        tag=get_object_or_404(Tag,slug=tag_slug)
        posts=posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 3) # Show 25 contacts per page.
   
    page_number = request.GET.get('page') 
    page = paginator.get_page(page_number) 
    
    #print("Hello",page_number, page)
    
        
        
 
    
    context={
        'posts': posts,
        'page':page,
        'tag':tag,
        'common_tags':common_tags,
        
             
     }
   
    return render(request,'blog_list.html',context)


def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    #comments 
    comments=post.comments.filter(active=True)
    tags=None
    tags=post.tags.all()
    new_comment=None
    if request.method == 'POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_form=CommentForm()
    

        
        
    post_tags_ids=post.tags.values_list('id',flat=True)
    similar_posts=Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:3]
    return render(request,'blog_details.html',{'post':post,
                                               'tags':tags,
                                                'comments':comments,'new_comment':new_comment,
                                                'comment_form':comment_form,
                                                'similar_posts':similar_posts,
                                                 })



def post_share(request,post_id):
    #get the post by id
    post=get_object_or_404(Post,id=post_id,status='published')
    sent=False
    if request.method =='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():  #see forms.errors 
            #fields passed the validation
            cleaned_data=form.cleaned_data
            #now can send email
            post_url=request.build_absolute_uri( post.get_absolute_url())
            subject= f"{cleaned_data['name']} recommends you read "\
                 f"{post.title}"
            message=f"Read {post.title} at {post_url}\n\n"\
                f"{cleaned_data['name']}\'s comments :{cleaned_data['comments']}"
            send_mail(subject,message,'melzpereira0509@gmail.com',
                      [cleaned_data['to']])
            sent=True
    else:
        #not a post request
        form=EmailPostForm()
    context={
        'post':post,
        'form':form,
        'sent':sent,
    }
    return render(request,'share.html',context)


def post_search(request):

    if 'search_post' in request.GET:
        
        search_post=request.GET['search_post']
        if search_post:
            print(search_post,"Melodyyy")
            queryset_post=Post.published.order_by('-publish').filter(body__icontains=search_post)
            print(queryset_post)
    else:
        queryset_post=None
    return render(request,'search_post.html', { 'ql_post':queryset_post } )