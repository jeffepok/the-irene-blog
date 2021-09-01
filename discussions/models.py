from django.db import models
from django.utils import timezone
from django.conf import settings as dj_settings
from djangocms_blog.models import BlogCategory
from django.utils.translation import gettext_lazy as _
from cms.models import CMSPlugin

# Create your models here.
class Discussion(models.Model):
    creator = models.ForeignKey(dj_settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True,
                               related_name="discussions", verbose_name=_("creator"))
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name="discussions", null=True, blank=True)
    title = models.CharField(_("title"), max_length=255)
    subject = models.TextField(null=True, blank=True)
    is_approved = models.BooleanField(_("approved"), default=False)
    primary_image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(_("created at"), auto_now_add=True)
    date_approved = models.DateTimeField(_("approved since"), null=True, blank=True)
    end_discussion_date = models.DateTimeField(_("active until"), null=True, blank=True)
    sort = models.PositiveSmallIntegerField(default=1000)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['sort', 'date_created']

    def save(self, *args, **kwargs):
        self.date_approved = (timezone.now() if self.date_approved else None)
        self.end_discussion_date = (None if self.end_discussion_date else timezone.now())
        super().save(*args, **kwargs)


class Comment(models.Model):
    poster = models.ForeignKey(dj_settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True,
                            related_name="comments", verbose_name=_("poster"))
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    date_created = models.DateTimeField(_("created at"), auto_now_add=True)
    primary_image = models.ImageField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.poster

    class Meta:
        ordering = ['date_created']


class DiscussionPluginModel(CMSPlugin):
    templates = dj_settings.DISCUSSION_PLUGIN_TEMPLATES
    rendering_template = models.CharField(
        max_length=255,
        choices=templates,
        default=templates[0][0],
        help_text=_("Select plugin template to load for this instance"),
    )