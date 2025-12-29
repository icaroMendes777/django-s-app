from django.contrib import admin
from .models import Petition

@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)

