from django.contrib import admin

from AirlineApp.models import Fly, Pilot, Airline


# Register your models here.
class FlyAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.creator=request.user
        super().save_model(self, request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.creator:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Fly, FlyAdmin)

class PilotInline(admin.StackedInline):
    model = Pilot
    extra = 1

class AirlineAdmin(admin.ModelAdmin):
    inlines = [PilotInline]
    list_display = ['name',]
admin.site.register(Airline, AirlineAdmin)