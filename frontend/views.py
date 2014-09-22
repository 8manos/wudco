from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import SponsorForm

def page(request, page):
  template = 'front/' + page + '.html'
  if page == 'formulario':
  	if request.method == 'POST':
  		form = SponsorForm(request.POST)
  		if form.is_valid():
  			pass
  	else:
  		form = SponsorForm()
  	return render(request, template, {'form': form,})
  else:
  	return render(request, template)