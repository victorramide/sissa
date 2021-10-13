from django.contrib import admin
from .models import Advogado


class ListandoAdvogados(admin.ModelAdmin):
    list_display = ('user', 'user_email', 'oab', 'uf')
    list_display_links = ('user',)
    search_fields = ('user',)
    list_per_page = 10

    @admin.display(ordering='user_email')
    def user_email(self, obj):
        return obj.user.email


admin.site.register(Advogado, ListandoAdvogados)
