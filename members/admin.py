from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin (admin.ModelAdmin):
    list_display=("firstname","lastname","homeuniversity","major")

admin.site.register(Member,MemberAdmin)