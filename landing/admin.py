from django.contrib import admin

# Register your models here.
from .models import Speaker, Sponsor, Talk, PotentialSponsor, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'published')
    list_editable = ('published', )
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Talk)
admin.site.register(PotentialSponsor)
admin.site.register(Post, PostAdmin)
