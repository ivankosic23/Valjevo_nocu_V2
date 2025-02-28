from django.contrib import admin
from .models import Svirka,Kafic
# Register your models here.
class kafic(admin.ModelAdmin):
    list_display=('ID','Ime','photo')
admin.site.register(Svirka)
admin.site.register(Kafic,kafic)