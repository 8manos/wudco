from django.contrib import admin

# Register your models here.
from .models import Speaker, Sponsor, Talk, PotentialSponsor,\
    Post, TeamMember, AgendaItem


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'published')
    list_editable = ('published', )
    prepopulated_fields = {"slug": ("title",)}


class AgendaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'item_type', 'time_starts',
                    'time_ends', 'coffee_break_after')
    list_editable = list_display[2:]

admin.site.register(Speaker)
admin.site.register(TeamMember)
admin.site.register(Sponsor)
admin.site.register(Talk)
admin.site.register(PotentialSponsor)
admin.site.register(Post, PostAdmin)
admin.site.register(AgendaItem, AgendaItemAdmin)
