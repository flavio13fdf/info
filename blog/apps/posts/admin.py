from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'contenido', 'fecha_creacion')
	list_filter = ('titulo','contenido')
# Register your models here.
admin.site.register(Post,PostAdmin)

