from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView
from django.utils.translation import gettext as _
from social_django.models import UserSocialAuth
from github.api import GitHubAPI
from .forms import CopyRepoForm


class MainPage(TemplateView):
    template_name = 'main_page.html'
    form = None
    github = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        try:
            self.github = GitHubAPI(request.user)
        except UserSocialAuth.DoesNotExist:
            messages.error(request, _('Please login via GitHub account'))
            return redirect('login')
        self.form = CopyRepoForm(request.user, request.POST or None, initial={
            'name': 'DataRobotTest',
            'description': 'My first self-replicated repo!',
            'homepage': 'http://localhost:8000/'
        })
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            repo = self.github.create_repo(self.form.cleaned_data)
            skip, repo_url = repo['git_url'].split('://')
            self.github.git_push(repo_url)
            messages.success(request, _('Repo copied successfully'))
            return redirect(request.path)
        return self.get(request, *args, **kwargs)


class GitHubLoginRedirectView(RedirectView):
    url = reverse_lazy('social:begin', kwargs={'backend': 'github'})

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
