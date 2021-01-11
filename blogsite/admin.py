from django.contrib import admin
from .models import BlogAuthor,BlogPost,BlogComment
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'date')
    search_fields = ('title','content','author')
    list_filter = ('author','date')

    class Meta:
        model = BlogPost

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('author','blog','comment','comment_date')

    class Meta:
        model = BlogComment


admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)
admin.site.register(BlogAuthor)