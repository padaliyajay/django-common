from django.contrib import admin

from .models import Post, Author, Category, Comment

# Post
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_added'
    list_display = ['title', 'status', 'author', 'sort_order', 'date_modified']
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)

# Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
admin.site.register(Author)

# Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort_order', 'status', 'date_added']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

# Comment
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_added'
    list_display = ['name', 'reply_to', 'post', 'date_added']
    autocomplete_fields = ['post']

    class Meta:
        verbose_name_plural = 'comments'
        
admin.site.register(Comment, CommentAdmin)
