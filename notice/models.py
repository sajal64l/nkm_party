from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from parler.managers import TranslatableQuerySet, TranslatableManager

from flipbook.models import PdfFlipbook


#Adding custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')


class Post(TranslatableModel):
    STATUS_CHOICES = (
        (_('draft'), _('draft')),
        (_('published'), _('published')),
    )
    slug = models.SlugField(max_length=250, unique_for_date='publish', null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='notice_posts', null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    flipbook = models.ForeignKey(PdfFlipbook, on_delete=models.CASCADE, related_name="flipbook", blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft', null=True, blank=True)
    image = models.ImageField(upload_to='notice/images/', null=True, blank=True)

    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=255, null=True, blank=True),
        body = models.TextField(_('body'), null=True, blank=True),
    )
    tags = TaggableManager()

    class Meta:
        # ordering = ('-publish',)
        verbose_name = _('notice')
        verbose_name_plural = _('notice')

    
    def get_absolute_url(self):
        return reverse('notice:post_detail', args=[self.publish.year,
                    self.publish.month,
                    self.publish.day, self.slug])

    

class Comment(models.Model):
    post = models.ForeignKey(Post, 
                            on_delete=models.CASCADE, 
                            related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now =True)
    # active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'    

