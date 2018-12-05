from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from .signals import save_comment
import uuid
import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


@python_2_unicode_compatible
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    uploadedImage = models.ImageField(
        upload_to='Uploads/%Y/%m/', db_column="Upload an Image")
    title = models.CharField(max_length=200, verbose_name=_("title"))
    slug = models.SlugField()
    bodytext = models.TextField(verbose_name=_("message"))

    post_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("post date"))
    modified = models.DateTimeField(null=True, verbose_name=_("modified"))
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  verbose_name=_("posted by"))

    allow_comments = models.BooleanField(
        default=True, verbose_name=_("allow comments"))
    comment_count = models.IntegerField(
        blank=True, default=0, verbose_name=_('comment count'))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('blog_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        imageTemproary = Image.open(self.uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        imageTemproaryResized.save(outputIoStream , format='JPEG', quality=85)
        outputIoStream.seek(0)
        self.uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" %self.uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        super(Post, self).save(*args, **kwargs)
    
@python_2_unicode_compatible
class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE, verbose_name=_("post"))
    bodytext = models.TextField(verbose_name=_("message"))

    post_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("post date"))
    ip_address = models.GenericIPAddressField(
        default='0.0.0.0', verbose_name=_("ip address"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name=_("user"), related_name='comment_user')
    user_name = models.CharField(
        max_length=50, default='anonymous', verbose_name=_("user name"))
    user_email = models.EmailField(blank=True, verbose_name=_("user email"))

    def __str__(self):
        return self.bodytext

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['post_date']


post_save.connect(save_comment, sender=Comment)
