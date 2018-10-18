from django.contrib import admin
from .models import *
class CardsAdmin(admin.ModelAdmin):
    # list_display = ["name","email"]
    list_display = [field.name for field in Card._meta.fields]
    search_fields = ['title']
    class Meta:
        model = Card


admin.site.register(Card, CardsAdmin)


class TagsAdmin(admin.ModelAdmin):
    # list_display = ["name","email"]
    list_display = [field.name for field in Tag._meta.fields]
    search_fields = ['title']
    class Meta:
        model = Tag


admin.site.register(Tag, TagsAdmin)