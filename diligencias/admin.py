from django.contrib import admin
from diligencias.models import Diligencia


class ListandoDiligencias(admin.ModelAdmin):
    list_display = ('processo', 'advogado', 'classe', 'data_diligencia')
    list_display_links = ('processo',)
    list_filter = ('advogado',)
    list_per_page = 10


admin.site.register(Diligencia, ListandoDiligencias)