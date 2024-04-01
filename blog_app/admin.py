"""
Admin Site for the blog_app app.
"""

from django.contrib import admin

from .models import Post, Category, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    """
    Custom admin site for the Post model.
    """
    list_display = ('title', 'category', 'publish_date')
    list_filter = ('publish_date', 'category')
    search_fields = ('title',)
    date_hierarchy = 'publish_date'

class CommentAdmin(admin.ModelAdmin):
    """
    Custom admin site for the Comment model.
    """
    list_display = ('post', 'author', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('text', 'author__username', 'post__title')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)