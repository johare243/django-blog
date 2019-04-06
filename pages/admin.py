from django.contrib import admin
from pages.models import Category, Post, UserProfile
# from django_markdown.widgets import MarkdownWidget

class PostAdmin(admin.ModelAdmin):
    fields=['category','title','views','text','post_image','summary']

class CategoryAdmin(admin.ModelAdmin):
    populated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)

