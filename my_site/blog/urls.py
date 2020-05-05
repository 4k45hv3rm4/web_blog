from django.urls import path
from blog.views import post_detail, post_list
app_name= 'blog'
from .feeds import LatestPostFeed
urlpatterns = [
        path('', post_list, name="post_list"),
        path('tag/<slug:tag_slug>', post_list, name="post_list_by_tag"),

        path('<int:year>/<int:month>/<int:day>/<slug:post>',
                post_detail,
                name='post_detail'),
        path('feed/', LatestPostFeed(), name="post_feed")

        ]
