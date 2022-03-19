from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    
    CATEGORY_CHOICES = (
        ('science', 'Science'),
        ('tech', 'Tech'),
        ('health', 'Health'),
        ('fashion', 'Fashion'),
        ('beauty', 'Beauty'),
        ('arts & lifestyle', 'Arts & Lifesyle'),
        ('news', 'News'),
        ('fiction', 'Fiction'),

    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='posts')
    body = models.TextField()
    post_category = models.CharField(max_length=20,
                                    choices=CATEGORY_CHOICES,)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
                                
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
                            

class Comment(models.Model):
    post = models.ForeignKey(Post,
                            on_delete=models.CASCADE,
                            related_name='posts')
    name = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
