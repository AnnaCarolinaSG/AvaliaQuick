from django.contrib import admin
from avaliaquick.models import Pendentes, Pesquisador, AvaliacaoAnual, CustomUser

admin.site.register(CustomUser)
admin.site.register(Pendentes)
admin.site.register(Pesquisador)
admin.site.register(AvaliacaoAnual)
# Register your models here.
