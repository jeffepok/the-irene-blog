from django import forms
from discussions.models import Discussion


class DiscussionAdminForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['creator', 'title', 'category', 'subject', 'primary_image', 'is_active', 
                'is_approved']
        exclude = ['end_discussion_date', 'date_approved']
