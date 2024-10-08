from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime
from common.models import TimeStampedModel

class Post(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=50)
    content = models.TextField(_('Content'))
    tags = models.CharField(_('Tags'), max_length=200)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')

    def get_total_likes(self):
        return Like.objects.filter(post=self).count()

class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return f"{self.user.username} commented on post {self.post.id}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post'), ('user', 'comment')