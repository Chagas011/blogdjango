from django.contrib import admin

# Register your models here.

from .models import Perfils


@admin.register(Perfils)
class PerfilsAdmin(admin.ModelAdmin):
    pass
