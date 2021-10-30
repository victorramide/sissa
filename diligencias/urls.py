from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_diligencias', views.lista_diligencias, name='lista_diligencias'),
    path('minhas_diligencias', views.minhas_diligencias, name='minhas_diligencias'),
    path('cadastra_diligencia', views.cadastra_diligencia, name='cadastra_diligencia'),
    path('deleta_diligencia/<int:diligencia_id>', views.deleta_diligencia, name='deleta_diligencia'),
    path('edita_diligencia/<int:diligencia_id>', views.edita_diligencia, name='edita_diligencia'),
    path('atualiza_diligencia', views.atualiza_diligencia, name='atualiza_diligencia')
]
