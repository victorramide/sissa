from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('minhas_diligencias', views.minhas_diligencias, name='minhas_diligencias'),
    path('cadastra_diligencia', views.cadastra_diligencia, name='cadastra_diligencia'),
    path('deleta_diligencia/<int:diligencia_id>', views.deleta_diligencia, name='deleta_diligencia')
]