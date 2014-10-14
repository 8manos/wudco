from django.contrib import admin

# Register your models here.
from .models import Speaker, Sponsor, Talk, PotentialSponsor,\
    Post, TeamMember, AgendaItem, NearbyPlace, PastEdition


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'published')
    list_editable = ('published', )
    prepopulated_fields = {"slug": ("title",)}


class AgendaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'item_type', 'time_starts',
                    'time_ends', 'coffee_break_after')
    list_editable = list_display[2:]


class NearbyPlaceAdmin(admin.ModelAdmin):
    list_display = ('place_type', 'name', 'order', )
    list_editable = ('order', )


class PastEditionAdmin(admin.ModelAdmin):
    list_display = ('year', 'description', 'youtube_id', 'image', )


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_partner', 'order')
    list_editable = ('is_partner', 'order')


admin.site.register(Speaker)
admin.site.register(PastEdition, PastEditionAdmin)
admin.site.register(NearbyPlace, NearbyPlaceAdmin)
admin.site.register(TeamMember)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Talk)
admin.site.register(PotentialSponsor)
admin.site.register(Post, PostAdmin)
admin.site.register(AgendaItem, AgendaItemAdmin)
