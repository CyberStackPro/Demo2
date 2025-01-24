from django.contrib import admin
from .models import Tag
from .models import TaggedItem

# Register your models here.

# admin.site.register(Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['tag']
    search_fields = ['label']
