from django import forms
from django.utils.translation import gettext as _
from github.api import GitHubAPI


class CopyRepoForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)
    homepage = forms.URLField(required=False)
    has_issues = forms.BooleanField(required=False)
    has_projects = forms.BooleanField(required=False)
    has_wiki = forms.BooleanField(required=False)

    def __init__(self, user, *args, **kwargs):
        self.github = GitHubAPI(user)
        super().__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data['name']
        if self.github.repo_exists(name):
            raise forms.ValidationError(_('Repo with current name already exists'), code='invalid')
        return name
