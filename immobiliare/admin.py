from django.contrib import admin
from .models import Agenti, Proprietari, Clienti, Immobili, Appuntamenti

# Register your models here.
admin.site.register(Agenti)
admin.site.register(Proprietari)
admin.site.register(Clienti)
admin.site.register(Immobili)
admin.site.register(Appuntamenti)
