from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Speaker, Sponsor, Talk, Post, TeamMember, AgendaItem, NearbyPlace
from .forms import SponsorForm

from django.core.urlresolvers import reverse


FECHA_CIERRE = date(2014, 11, 7)
PRICE_BEFORE = 60000
PRICE_AFTER = 80000


def get_context(request):
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
    data['price_before'] = PRICE_BEFORE
    data['price_after'] = PRICE_AFTER
    return data


def home(request):
    try:
        data = get_context(request)
        # print data
        data['speakers'] = Speaker.objects.filter(only_workshop=False)
        data['sponsors'] = Sponsor.objects.all()
        data['talks'] = Talk.objects.all()
        data['posts'] = Post.objects.filter(published=True)[:2]
        data['days_left'] = max((FECHA_CIERRE - date.today()).days, 0)
    except:
        pass
    return render(request, 'front/index.html', data)


def event(request):
    data = get_context(request)
    data['team'] = TeamMember.objects.all()
    return render(request, 'front/evento.html', data)


def place(request):
    data = get_context(request)
    places = NearbyPlace.objects.all()
    d_places = {}
    for p in places:
        ps = d_places.get(p.get_place_type_display(), [])
        ps.append(p)
        d_places[p.get_place_type_display()] = ps
    data['places'] = d_places
    # data['team'] = TeamMember.objects.all()
    return render(request, 'front/lugar.html', data)


def agenda(request):
    data = get_context(request)
    data['agenda'] = AgendaItem.objects.all()
    data['speakers'] = Speaker.objects.filter(only_workshop=False)
    return render(request, 'front/programa.html', data)


def speakers(request):
    data = get_context(request)
    data['speakers'] = Speaker.objects.filter(only_workshop=False)
    return render(request, 'front/ponentes.html', data)


def workshops(request):
    data = get_context(request)
    data['speakers'] = Speaker.objects.filter(workshop_name__gt='')
    return render(request, 'front/talleres.html', data)


def post(request, post_slug=None):
    data = get_context(request)
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
    data = get_context(request)
    initial_d = {'subject': u'Quiero ser patrocinador'}
    if register_type and register_type == 'volunteer':
        initial_d = {'subject': u'Quiero ser voluntario'}
    form = SponsorForm(request.POST or None, auto_id='%s', label_suffix='', initial=initial_d)
    if form.is_valid():
        form.save()
        form = None
    data['form'] = form
    return render(request, 'front/formulario.html', data)
