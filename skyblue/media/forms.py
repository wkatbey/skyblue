from django import forms
from django.forms import ModelForm
from media.models import MediaEntry
from datetime import datetime

class MediaEntryForm(ModelForm):
    class Meta:
        model = MediaEntry
        fields = (
            'title',
            'description',
            'content',
        )

        widgets = {
            'description': forms.Textarea(
                attrs = {
                    'cols': 80, 
                    'rows': 20,
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'content': forms.FileInput(
                attrs = {
                    'class': 'custom-file-input'
                }
            ),
        }

    def save(self, commit=True):
        media_instance = super(MediaEntryForm, self).save(commit=False)
        media_instance.date_of_submission = datetime.now()
        media_instance.date_updated = datetime.now()

        return media_instance
