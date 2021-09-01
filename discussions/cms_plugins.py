from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from discussions.models import DiscussionPluginModel, Discussion
from django.utils.translation import gettext as _


@plugin_pool.register_plugin  # register the plugin
class DiscussionPluginPublisher(CMSPluginBase):
    model = DiscussionPluginModel  # model where plugin data are saved
    module = _("Discussions")
    name = _("Discussion Plugin")  # name of the plugin in the interface

    def render(self, context, instance, placeholder):
        # Get all approved and active discussions
        discussions = Discussion.objects.filter(is_active=True, is_approved=True)
        context.update({'discussions': discussions})
        return context

    def get_render_template(self, context, instance, placeholder):
        return instance.rendering_template

