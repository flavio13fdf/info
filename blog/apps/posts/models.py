from django.db import models
from django.utils import timezone
from apps.accounts.models import Author
from tinymce.models import HTMLField


# Create your models here.

class Post(models.Model):

    titulo= models.CharField(max_length=200)
    contenido= models.TextField(max_length=500)
    fecha_creacion= models.DateTimeField(default=timezone.now)
    fecha_publicacion= models.DateTimeField(blank=True, null=True)
    autor = models.ForeignKey(Author, verbose_name="autor", on_delete=models.CASCADE)
    slug = models.SlugField("Slug", blank=True, null=True)
    
    class meta:
        verbose_name= "Post"
        verbose_name_plural="Publicaciones"
    
    def __str__(self) -> str:
        return self.titulo



class Comentario(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	contenido = models.TextField() 
	fecha_hora = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.contenido

	class Meta:
		verbose_name = ("Comentario")
		verbose_name_plural= ("Comentarios")