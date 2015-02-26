from django.contrib import admin

# Register your models here.
from .models import Speaker, Sponsor, Talk, PotentialSponsor,\
    Post, TeamMember, AgendaItem, NearbyPlace, PastEdition,\
    PlaceInfo, PostEventPhoto, PostEventVideo


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


class PlaceInfoAdmin(admin.ModelAdmin):
    list_display = ('title', )


class PostEventPhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'order')
    list_editable = ('order', )


class PostEventVideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_url', 'order')
    list_editable = ('order', )

admin.site.register(PostEventPhoto, PostEventPhotoAdmin)
admin.site.register(PostEventVideo, PostEventVideoAdmin)
admin.site.register(Speaker)
admin.site.register(PlaceInfo, PlaceInfoAdmin)
admin.site.register(PastEdition, PastEditionAdmin)
admin.site.register(NearbyPlace, NearbyPlaceAdmin)
admin.site.register(TeamMember)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Talk)
admin.site.register(PotentialSponsor)
admin.site.register(Post, PostAdmin)
admin.site.register(AgendaItem, AgendaItemAdmin)
