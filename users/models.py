from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from common.models import TimeStampedModel
from posts.models import Post
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username')

class Bookmarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
