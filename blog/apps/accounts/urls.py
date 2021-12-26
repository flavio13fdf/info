from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.accounts import views

urlpatterns = [
    path(
        'accounts/register/', views.AuthorCreateView.as_view(), name='accounts_register'
    ),
] 