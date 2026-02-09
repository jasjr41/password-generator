from django.contrib import admin

from app1.models import Person


# Register your models here.
class Admin(admin.ModelAdmin):
    list_filter = ["length"]
    list_display = ["length"]
admin.site.register(Person, Admin)