from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True) 
    modified_at = models.DateTimeField(_('Modified At'), auto_now=True)
    deleted_at = models.DateTimeField(_('Deleted At'), null=True, blank=True)

    class Meta: 
        abstract = True

    def delete(self, *args, **kwargs):
        """Soft deletes a record"""
        self.deleted_at = timezone.now() 
        self.save()

    def save(self, *args, **kwargs):
        """Override save to set the modified_at field."""
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super().save(*args, **kwargs)

    @classmethod
    def all(cls):
        return cls.objects.filter(deleted_at__isnull=True)
