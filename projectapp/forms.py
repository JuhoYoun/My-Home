from django.forms import ModelForm
from django import forms
from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'id': 'image-upload'}))

    class Meta:
        model = Project
        fields = ['image', 'title', 'description']