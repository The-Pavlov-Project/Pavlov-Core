from django.contrib import admin
from .models import Event


@admin.register(Event)
class CurrencyWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'start_time', 'end_time')
    list_filter = ('user',)
