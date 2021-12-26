from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post

class ListarPosts(ListView):	
	model= Post
	template_name = "posts/post_list.html"
	context_object_name = "posts"
    
	""" def get_queryset(self):
		noticias = Noticia.objects.all().order_by('-fecha_creacion')
		return noticias """
		
class DetallePosts(DetailView):
	model=Post
	template_name="posts/post_detail.html"		