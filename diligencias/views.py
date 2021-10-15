from django.shortcuts import render

from diligencias.models import Diligencia


def index(request):
    return render(request, 'index.html')


def diligencias(request):
    diligencias_comuns = Diligencia.objects.filter(prioridade=False).exclude(tipo='Sentença')
    diligencias_prioridade = Diligencia.objects.filter(prioridade=True).exclude(tipo='Sentença')
    diligencias_sentencas_comuns = Diligencia.objects.order_by('data_conclusao').filter(prioridade=False).filter(tipo='Sentença')
    diligencias_sentencas_prioridade = Diligencia.objects.order_by('data_conclusao').filter(prioridade=True).filter(tipo='Sentença')

    dados_diligencias = {
        'diligencias_comuns': diligencias_comuns,
        'diligencias_prioridade': diligencias_prioridade,
        'diligencias_sentencas_comuns': diligencias_sentencas_comuns,
        'diligencias_sentencas_prioridade': diligencias_sentencas_prioridade
    }
    return render(request, 'diligencias.html', dados_diligencias)


