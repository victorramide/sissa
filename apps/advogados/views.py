from django.contrib import messages, auth
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from apps.advogados.models import Advogado


def cadastro(request):
    # Pega todos os campos do fomulário e salva em variáveis
    if request.method == 'POST':
        primeiro_nome = request.POST['primeiro_nome']
        ultimo_nome = request.POST['ultimo_nome']
        email = request.POST['email']
        oab = request.POST['oab']
        uf = request.POST['uf']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        # Salva como username o primeiro e ultimo nome do usuário.
        username = f'{primeiro_nome} {ultimo_nome}'
        # Faz a validação dos dados verificando se os campos não estão vazios ou se existe usuário com aquele email
        # ou username
        if campo_vazio(primeiro_nome):
            messages.error(
                request, 'O campo primeiro nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(ultimo_nome):
            messages.error(
                request, 'O campo ultimo nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(oab):
            messages.error(request, 'Número de OAB é obrigatório')
            return redirect('cadastro')

        if campo_vazio(uf):
            messages.error(request, 'O campo UF nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')

        # Criação do usuário com base no modelo padrão do Django
        user = User.objects.create_user(username=username, email=email, password=senha, first_name=primeiro_nome,
                                        last_name=ultimo_nome)

        # recuperando o username do usuário para utilizar no cadastro do perfil de Advogado
        id_usuario = User.objects.get(username=username)

        # Salvando o usuário e o perfil de Advogado com os dados específicos
        advogado = Advogado(user=id_usuario, oab=oab, uf=uf)
        user.save()
        advogado.save()

        # Envia a mensagem de sucesso e redireciona para a página de Login
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        # Caso o cadastro não seja realizado o sistema se mantem na
        return render(request, 'advogados/cadastro.html')
        # página de Cadastro


def login(request):
    # Pega os campos do formulário de Login
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        # verifica se os campos foram preenchidos
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha são obrigatórios')
            return redirect('login')

        # Método para recuperar o username através do email digitado, permitindo a autenticação por e-mail
        # primeiro verifica se o email existe.
        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username',
                                                                    flat=True).get()  # pega o username vinculado ao
            # email
            # Salva o usuário na variável
            user = auth.authenticate(
                request, username=username, password=senha)
            if user is not None:  # Caso o usuário não esteja vazio, ou seja, ele exista.
                auth.login(request, user)  # Realiza a autenticação do usuário
                return redirect('index')
        # Caso não seja possível recuperar o usuário exibe mensagem de erro
        messages.error(
            request, 'Falha na autenticação, verifique seu email e senha')
    return render(request, 'advogados/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def campo_vazio(campo):
    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2
