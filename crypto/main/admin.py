from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_display_links = ['name']
    prepopulated_fields = {'slug':('name',)}
        