from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from advogados.models import Advogado
from advogados.views import campo_vazio
from diligencias.models import Diligencia


def index(request):
    return render(request, 'index.html')


def lista_diligencias(request):
    diligencias_comuns = Diligencia.objects.filter(prioridade=False).exclude(tipo='Sentença')
    diligencias_prioridade = Diligencia.objects.filter(prioridade=True).exclude(tipo='Sentença')
    diligencias_sentencas_comuns = Diligencia.objects.order_by('data_conclusao').filter(prioridade=False).filter(
        tipo='Sentença')
    diligencias_sentencas_prioridade = Diligencia.objects.order_by('data_conclusao').filter(prioridade=True).filter(
        tipo='Sentença')

    dados_diligencias = {
        'diligencias_comuns': diligencias_comuns,
        'diligencias_prioridade': diligencias_prioridade,
        'diligencias_sentencas_comuns': diligencias_sentencas_comuns,
        'diligencias_sentencas_prioridade': diligencias_sentencas_prioridade
    }
    return render(request, 'diligencias/lista_diligencias.html', dados_diligencias)


def minhas_diligencias(request):
    advogado = get_object_or_404(Advogado, user_id=request.user.id)

    diligencias = Diligencia.objects.filter(advogado_id=advogado)
    diligencias_a_exibir = {
        'diligencias': diligencias
    }
    return render(request, 'diligencias/minhas_diligencias.html', diligencias_a_exibir)


def cadastra_diligencia(request):
    if request.method == 'POST':
        processo = request.POST['processo']
        classe = request.POST['classe']
        tipo = request.POST['tipo']
        descricao_diligencia = request.POST['diligencia']
        prioridade = request.POST['prioridade']
        advogado = get_object_or_404(Advogado, user_id=request.user.id)
        data_conclusao = request.POST['data_conclusao']

        if campo_vazio(processo):
            messages.error(request, 'O campo processo não pode ficar em branco')
            return redirect('cadastra_diligencia')

        if campo_vazio(classe):
            messages.error(request, 'Selecione uma classe processual')
            return redirect('cadastra_diligencia')

        if campo_vazio(tipo):
            messages.error(request, 'Selecione um tipo de diligência')
            return redirect('cadastra_diligencia')

        if campo_vazio(data_conclusao):
            messages.error(request, 'A data de conclusão do processo é obrigatória')
            return redirect('cadastra_diligencia')

        diligencia = Diligencia.objects.create(processo=processo, classe=classe, tipo=tipo,
                                               diligencia=descricao_diligencia, prioridade=prioridade,
                                               advogado=advogado, data_conclusao=data_conclusao)
        diligencia.save()
        messages.success(request, 'Diligência cadastrada com sucesso!')
        return redirect('index')
    else:
        return render(request, 'diligencias/cadastra_diligencia.html')


def deleta_diligencia(request, diligencia_id):
    diligencia = get_object_or_404(Diligencia, pk=diligencia_id)
    diligencia.delete()
    return redirect('minhas_diligencias')


def edita_diligencia(request, diligencia_id):
    diligencia = get_object_or_404(Diligencia, pk=diligencia_id)
    diligencia_a_editar = {'diligencia': diligencia}
    return render(request, 'diligencias/edita_diligencia.html', diligencia_a_editar)


def atualiza_diligencia(request):
    if request.method == 'POST':
        diligencia_id = request.POST['diligencia_id']
        diligencia = Diligencia.objects.get(pk=diligencia_id)
        diligencia.processo = request.POST['processo']
        diligencia.classe = request.POST['classe']
        diligencia.tipo = request.POST['tipo']
        diligencia.prioridade = request.POST['prioridade']
        diligencia.diligencia = request.POST['diligencia']
        if request.POST['data_conclusao'] != "":
            diligencia.data_conclusao = request.POST['data_conclusao']
        diligencia.save()
        return redirect('minhas_diligencias')
