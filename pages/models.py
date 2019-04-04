from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    cat_image = models.ImageField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    text = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    summary = models.TextField(null=True, blank=True)
    post_image = models.ImageField(null=True,blank=True)
    created_date = models.DateTimeField(default=now, editable=False)
    publish = models.BooleanField(default=True)

    #custom query manager command
    #to return only published posts
    objects = PostQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
