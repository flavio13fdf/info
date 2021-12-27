from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from apps.posts.models import Post, Comentario
from tinymce.widgets import TinyMCE
class PostForm(forms.ModelForm):

	content = forms.CharField(label="Contenido", 
		widget=TinyMCE(attrs={"cols":80, "rows": 15, "class":"form-control"})
	)

	class Meta:
		model= Post
		fields = ('autor', 'titulo', 'contenido',)

""" 	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper() """
class Comentario(forms.ModelForm):

	class Meta:
		model: Comentario
		fiels = ("contenido",)
