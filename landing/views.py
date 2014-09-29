from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Speaker, Sponsor, Talk, Post
from .forms import SponsorForm


FECHA_CIERRE = date(2014, 11, 7)


def home(request):
    data = {}
    data['speakers'] = Speaker.objects.all()
    data['sponsors'] = Sponsor.objects.all()
    data['talks'] = Talk.objects.all()
    data['days_left'] = max((FECHA_CIERRE - date.today()).days, 0)
    return render(request, 'index.html', data)


def speakers(request):
    data = {}
    data['speakers'] = Speaker.objects.all()
    return render(request, 'front/ponentes.html', data)


def workshops(request):
    data = {}
    data['speakers'] = Speaker.objects.filter(workshop_name__gt='')
    return render(request, 'front/talleres.html', data)


def post(request, post_slug=None):
    data = {}
    if post_slug:
        post = get_object_or_404(Post, slug=post_slug)
    else:
        try:
            post = Post.objects.filter(published=True)[0]
        except:
            post = None
    if post:
        data['post'] = post
        data['more_posts'] = Post.objects.filter(published=True).exclude(id=post.id)[:3]
    return render(request, 'front/interna.html', data)


def sponsor_form(request, register_type=None):
    data = {}
    initial_d = {'subject': u'Quiero ser patrocinador'}
    if register_type and register_type == 'volunteer':
        initial_d = {'subject': u'Quiero ser voluntario'}
    form = SponsorForm(request.POST or None, auto_id='%s', label_suffix='', initial=initial_d)
    if form.is_valid():
        form.save()
        form = None
    data['form'] = form
    return render(request, 'front/formulario.html', data)
