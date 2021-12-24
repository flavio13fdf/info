from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarPosts.as_view(), name='listar'),
] 