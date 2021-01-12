from django.contrib import admin
from .models import BlogAuthor,BlogPost,BlogComment
# Register your models here.


class BlogCommentsInline(admin.TabularInline):
    model = BlogComment
    max_num=0

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'date')
    search_fields = ('title','content','author')
    list_filter = ('author','date')
    inlines = [BlogCommentsInline]

    class Meta:
        model = BlogPost


admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(BlogComment)
admin.site.register(BlogAuthor)