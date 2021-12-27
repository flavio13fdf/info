# from django.http import HttpResponse
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.db.models.base import Model
from django.urls.base import reverse
from django.views.generic import (
	TemplateView,
	CreateView,
	DeleteView,
	DetailView,
	ListView,
	UpdateView,
	View,)

from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from .forms import PostForm
from apps.posts.models import Post, Comentario
from apps.posts.forms import PostForm
from apps.accounts.models import Author


class ListarPosts(LoginRequiredMixin,ListView):	
    login_url = 'login'
    model= Post
	template_name = "posts/post_list.html"
	context_object_name = "posts"
    
	""" def get_queryset(self):
		noticias = Noticia.objects.all().order_by('-fecha_creacion')
		return noticias """

def home(request):
	return render(request, 'home.html', {})

		
class DetallePosts(DetailView):
	model=Post
	template_name="posts/post_detail.html"	

class CrearPost(CreateView):
	model=Post
	# success_url='crear/'
	# fields= ['titulo','contenido']
	template_name = "blog/post_form.html"
	form_class = PostForm

	def form_valid(self, form):
		form.instance.author = Author.objects.filter(user=self.request.user).first
		form.save()
		return redirect(reverse("detalle", kwargs={"slug":form.instance.slug}))


class UpdatePost(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/blog_update_form.html'
	success_url='/lista'

class DeletePost(DeleteView):
	model = Post
	success_url = reverse_lazy('lista')
	