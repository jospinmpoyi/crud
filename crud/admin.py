from django.contrib import admin
from .models import Faculte,Etudiant
# Register your models here.
class FaculteAdmin(admin.ModelAdmin):
    list_display = ("libfac",)

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ("nom","postnom","prenom","telephone","faculte",)

admin.site.register(Faculte,FaculteAdmin)
admin.site.register(Etudiant,EtudiantAdmin)

