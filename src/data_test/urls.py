from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.flatpages import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('repo.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('', include('social_django.urls', namespace='social')),
    path('<path:url>', views.flatpage),
]
