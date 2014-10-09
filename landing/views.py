from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Speaker, Sponsor, Talk, Post, TeamMember, AgendaItem
from .forms import SponsorForm

from django.core.urlresolvers import reverse


FECHA_CIERRE = date(2014, 11, 7)


def get_menu(request):
    menu = [
            {'url': "/", 'name': 'Inicio'},
            {'url': reverse('event'), 'name': 'El evento'},
            {'url': reverse('speakers'), 'name': 'Ponentes'},
            {'url': reverse('agenda'), 'name': 'Programa'},
            {'url': reverse('workshops'), 'name': 'Talleres'},
            {'url': reverse('place'), 'name': 'Lugar'},
            {'url': reverse('blog'), 'name': 'Blog wudco'},
    ]
    data = {'menu': menu}
    for item in data['menu']:
        if request.path == item['url']:
            item['active'] = True
        else:
            item['active'] = False
    return data


def home(request):
    data = get_menu(request)
    data['speakers'] = Speaker.objects.all()
    data['sponsors'] = Sponsor.objects.all()
    data['talks'] = Talk.objects.all()
    data['days_left'] = max((FECHA_CIERRE - date.today()).days, 0)
    return render(request, 'front/index.html', data)


def event(request):
    data = get_menu(request)
    data['team'] = TeamMember.objects.all()
    return render(request, 'front/evento.html', data)


def place(request):
    data = get_menu(request)
    # data['team'] = TeamMember.objects.all()
    return render(request, 'front/lugar.html', data)


def agenda(request):
    data = get_menu(request)
    data['agenda'] = AgendaItem.objects.all()
    data['speakers'] = Speaker.objects.all()
    return render(request, 'front/programa.html', data)


def speakers(request):
    data = get_menu(request)
    data['speakers'] = Speaker.objects.all()
    return render(request, 'front/ponentes.html', data)


def workshops(request):
    data = get_menu(request)
    data['speakers'] = Speaker.objects.filter(workshop_name__gt='')
    return render(request, 'front/talleres.html', data)


def post(request, post_slug=None):
    data = get_menu(request)
    data['menu'][-1]['active'] = True
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
    data = get_menu(request)
    initial_d = {'subject': u'Quiero ser patrocinador'}
    if register_type and register_type == 'volunteer':
        initial_d = {'subject': u'Quiero ser voluntario'}
    form = SponsorForm(request.POST or None, auto_id='%s', label_suffix='', initial=initial_d)
    if form.is_valid():
        form.save()
        form = None
    data['form'] = form
    return render(request, 'front/formulario.html', data)
