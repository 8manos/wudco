from django.shortcuts import render
from django.views.generic.base import TemplateView

def page(request, page):
  template = 'front/' + page + '.html'
  return render(request, template)
