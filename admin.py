from django.contrib import admin

from .models import IPAddress
# Register your models here.
@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
	list_display = ('car_name', 'ip', 'time')
