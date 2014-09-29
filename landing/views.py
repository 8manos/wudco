from datetime import date

from django.shortcuts import render

from .models import Speaker, Sponsor, Talk
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
    data['speakers'] = Speaker.objects.all()
    return render(request, 'front/talleres.html', data)


def sponsor_form(request):
    data = {}
    data['speakers'] = Speaker.objects.all()
    form = SponsorForm(request.POST or None, auto_id='%s', label_suffix='')
    if form.is_valid():
        form.save()
        form = None
    data['form'] = form
    return render(request, 'front/formulario.html', data)
