from django.contrib import admin
from .models import Post

# customizing admin section
class PostAdmin(admin.ModelAdmin):
    #setting the field to be displayed
    list_display = ('title', 'slug','status','author', 'publish')
    list_filter = ('status','created', 'publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug' : ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('publish','status')

admin.site.register(Post, PostAdmin)
