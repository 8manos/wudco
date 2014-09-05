from datetime import date

from django.shortcuts import render

from .models import Speaker, Sponsor, Talk

FECHA_CIERRE = date(2014, 11, 7)


def home(request):
    data = {}
    data['speakers'] = Speaker.objects.all()
    data['sponsors'] = Sponsor.objects.all()
    data['talks'] = Talk.objects.all()
    data['days_left'] = max((FECHA_CIERRE - date.today()).days, 0)
    return render(request, 'index.html', data)
