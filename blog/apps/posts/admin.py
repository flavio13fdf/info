from django.contrib import admin
from apps.posts.models import Post, Comentario
# Register your models here.

""" class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'contenido', )
	list_filter = ('titulo','contenido') """
# Register your models here.
# admin.site.register(Post,PostAdmin)

admin.site.register(Post)
admin.site.register(Comentario)

