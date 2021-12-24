from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    titulo= models.CharField(max_length=200)
    contenido= models.TextField(max_length=500)
    fecha_creacion= models.DateTimeField(default=timezone.now)
    fecha_publicacion= models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.titulo

    class meta:
        verbose_name= "Post"
        verbose_name_plural="Publicaciones"

class Comentario(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	contenido = models.TextField() 
	fecha_hora = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.contenido

	class Meta:
		verbose_name = ("Comentario")
		verbose_name_plural= ("Comentarios")