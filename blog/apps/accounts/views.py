from django.shortcuts import redirect, render
from django.views.generic import CreateView, View
from apps.accounts.forms import AuthorForm, UserForm
from apps.accounts.models import Author
from django.urls import reverse_lazy

class AuthorCreateView(CreateView):
	template_name = "accounts/author_form.html"
	form_class = UserForm
	success_url = reverse_lazy("login")

	def form_valid(self, form):
		user = form.save()
		Author.objects.create(user=user)
		return super.form_valid(form)
