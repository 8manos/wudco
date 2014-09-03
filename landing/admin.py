from django.contrib import admin

# Register your models here.
from .models import Speaker, Sponsor

admin.site.register(Speaker)
admin.site.register(Sponsor)
