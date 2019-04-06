from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from pages.models import Category, Post, UserProfile

class PostAdmin(admin.ModelAdmin):
    fields=['category','title','views','markdown', 'text','post_image','summary']

class CategoryAdmin(admin.ModelAdmin):
    populated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)

