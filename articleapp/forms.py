from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'id': 'image-upload'}))

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
