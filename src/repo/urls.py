from django.contrib.flatpages import views
from django.urls import path
from .views import MainPage, GitHubLoginRedirectView

app_name = 'repo'

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('github/login/', GitHubLoginRedirectView.as_view(), name='github_login'),
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
]
