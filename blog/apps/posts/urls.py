from django.urls import path
from . import views
from .views import DetallePosts

urlpatterns = [
    path('', views.ListarPosts.as_view(), name='listar'),
    path('<slug:pk>/detalle', views.DetallePosts.as_view(), name='detalle'),
] 