from .models import Post, Comment
from django.shortcuts import render
from .forms import UserForm, CommentForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            print("registered")
        else:print(user_form.errors)
    else:
        user_form=UserForm()
    return render(request, "blog/register.html",{'user_form':user_form,'registered':registered})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect

def post_list(request):
    posts = Post.published.all()

    paginator = Paginator(posts, 3) #3 posts per page
    page = request.GET.get('page')

    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                    'blog/post_list.html',
                    {'page':page,
                    'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                            status = 'published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day
                            )
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method=="POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()


    return render(request,'blog/post_detail.html', {'comments':comments,'post':post,'new_comment':new_comment, 'comment_form':comment_form})
