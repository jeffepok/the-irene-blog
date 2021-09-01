from django.contrib import admin
from discussions.models import Discussion, Comment
from discussions.forms import DiscussionAdminForm

# Register your models here.
@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['creator','title', 'is_approved', 'sort']
    actions = ['activate', 'deactivate']
    form = DiscussionAdminForm
    list_editable = ['sort']
    
    def activate(self, request, queryset):
        for discussion in queryset:
            if not discussion.is_active:
                discussion.is_active = True
                discussion.save()
                
    def deactivate(self, request, queryset):
        for discussion in queryset:
            if discussion.is_active:
                discussion.is_active = False
                discussion.save()

    def get_changeform_initial_data(self, request):
        return {'creator': request.user}

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['poster','body', 'date_created']