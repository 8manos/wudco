from django.contrib import admin

# Register your models here.
from .models import Speaker, Sponsor, Talk

admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Talk)
