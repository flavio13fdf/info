from django.urls import path
# from . import views
# from .views import CrearPost, DetallePosts, UpdatePost,DeletePost
from django.contrib.auth.decorators import login_required
from apps.posts import views


urlpatterns = [
    path('', views.home, name='home'),
    path('listar', views.ListarPosts.as_view(), name='listar'),
    path('<slug:pk>/detalle', views.DetallePosts.as_view(), name='detalle'),
	path('<slug:pk>/update', views.UpdatePost.as_view(), name='update'),
	path('<slug:pk>/delete', views.DetallePosts.as_view(), name='delete'),
	path('crear/', login_required(views.CrearPost.as_view()), name='crear')
] 
