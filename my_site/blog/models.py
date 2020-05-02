from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super( PublishedManager, self)\
                        .get_queryset()\
                        .filter(status='published'
                            )



class Post(models.Model):
    STATUS_CHOICES=(
            ('draft','Draft'),
            ('published','Published')
        )
    title = models.CharField(max_length=250)
    #short label to be used for URLs
    slug  = models.SlugField(max_length=250,
        unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")#many_to_one relationship with user model of django
    body = models.TextField()
    #time when post published
    publish = models.DateTimeField(default = timezone.now)
    #time when post was created
    created = models.DateTimeField(auto_now_add=True)
    #time when post was updated
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10,
                               choices=STATUS_CHOICES,
                               default='draft')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        #post ordering in descending using publish field
        ordering = ('-publish',)

    def __str__(self):
        #default human-readable representation of the object
        return self.title


