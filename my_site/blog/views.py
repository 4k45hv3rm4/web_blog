from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post
from django.shortcuts import render, get_object_or_404

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
    return render(request,'blog/post_detail.html', {'post':post})
