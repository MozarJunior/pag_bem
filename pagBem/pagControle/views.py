from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as log, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pagControle.models import Cliente, Estabelecimento, Plano, PlanoControle, EstabelecimentoCliente

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context)

def login(request):
    context = {}
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        user_id = user.id
        cliente = Cliente.objects.filter(user__id=user_id)
        estabelecimento = Estabelecimento.objects.filter(user_id=user_id)

        if estabelecimento.exists():
            log(request, user)
            return redirect("http://127.0.0.1:8000/estabelecimento")
        elif cliente.exists:
            log(request, user)
            return redirect("http://127.0.0.1:8000/cliente")
        else:
            return redirect("http://127.0.0.1:8000/")
    else:
        return  redirect("http://127.0.0.1:8000/")

def cadastro(request):
    context = {}
    return render(request, "register.html", context)

def register(request):
    context = {'response':''}
    nome = request.POST['nome']
    email = request.POST['email']
    password = request.POST['password']
    confirmPassword = request.POST['confirmPassword']

    if password == confirmPassword:
        user = User.objects.create_user(nome, email, password)

        cliente = Cliente(
            nome = nome,
            login = email,
            senha = password,
            ativo = False,
            criadoEm = date.today(),
            atualizadoEm = date.today(),
            user = User.objects.get(id=user.id)
        )
        cliente.save()
    else: 
        context = {'response':"A senha e o confirmar não são iguais"}

    return render(request, "register.html", context)


@login_required
def estabelecimento_index(request):
    pk = request.user.id
    planosClintes = PlanoControle.objects.filter(plano__estabelecimento__id=pk)
    plano = Plano.objects.filter(estabelecimento__id=pk)
    planos =  Plano.objects.all()
    context = {'clientes': planosClintes,
                'plano': plano,
                'planos': planos,
                'estabelecimentos': pk,}
    return render(request, "estabelecimento/index.html", context)

@login_required(login_url="http://127.0.0.1:8000/")
def cliente_index(request):
    # user = User.is_authenticated
    user = request.user.id
    cliente = Cliente.objects.get(user__id=user)
    estabelecimento_cliente = EstabelecimentoCliente.objects.get(cliente__id=cliente.id)
    if estabelecimento_cliente != None:
        estabelecimento = estabelecimento_cliente.estabelecimento.id
        plano = Plano.objects.filter(estabelecimento__id=estabelecimento)
        estabelecimentos = Estabelecimento.objects.all()
        context = {"estabeleciementos": estabelecimentos,
                "user": user,
                "plano": plano}
    else: 
        estabelecimentos = Estabelecimento.objects.all()
        context = {"estabeleciementos": estabelecimentos,
                    "user": user}
    return render(request, "cliente/index.html", context)


def create_plano(request):
    context = {'response':''}
    nome = request.POST['nome']
    valor = request.POST['valor']
    duracaoDias = request.POST['duracaoDias']
    frequencia = request.POST['frequencia']
    estabelecimento_id = request.POST['estabelecimento']

    estabelecimento = Estabelecimento.objects.get(id=estabelecimento_id)

    plano = Plano(
        nome = nome,
        valor = valor,
        duracaoDias = duracaoDias,
        frequencia = frequencia,
        estabelecimento = estabelecimento
    )

    if plano.save():
        context = {'response':"Cadastro no estabelecimento concluido"}
        return render(request, "cliente/index.html", context)
    else:
        context = {'response':"Não foi possivel cadastrar"}
        return render(request, "cliente/index.html", context)

def update_plano(request, pk):
    context = {}
    plano = Plano.objects.get(id=pk)
    if request.method == 'POST':
        nome = request.POST['nome']
        valor = request.POST['valor']
        duracaoDias = request.POST['duracaoDias']
        frequencia = request.POST['frequencia']
        plano.nome = nome
        plano.valor = valor
        plano.duracaoDias = duracaoDias
        plano.frequencia = frequencia
        plano.save()
    
    return redirect("url 'estabelecimento'")

def delete_plano(request, pk):
    plano = Plano.objects.get(id=pk)
    plano.delete()
    return redirect('http://127.0.0.1:8000/estabelecimento')

def cliente_estabelecimento(request):
    context = {'response': ''}
    cliente_id = request.POST['cliente']
    estabelecimento_id = request.POST['estabelecimento']
    estabelecimento = Estabelecimento.objects.get(id=estabelecimento_id)
    cliente = Cliente.objects.get(user__id=cliente_id)

    estabelecimentoCliente = EstabelecimentoCliente(
        cliente = cliente,
        estabelecimento = estabelecimento,
        ingresso = date.today()
    )
    estabelecimentoCliente.save()

    if estabelecimentoCliente:
        context = {'response':"Cadastro no estabelecimento concluido"}
        return render(request, "cliente/index.html", context)
    else:
        context = {'response':"Não foi possivel cadastrar"}
        return render(request, "cliente/index.html", context)
    


def cliente_plano(request):
    context = {'response': ''}
    plano_id = request.POST['plano']
    cliente_id = request.POST['cliente']
    plano = Plano.objects.get(id=plano_id)
    cliente = Cliente.objects.get(user__id=cliente_id)

    planoCliente = PlanoControle(
        ingresso = date.today(),
        vencimento = date.today,
        plano = plano,
        cliente = cliente
    )
    planoCliente.save()

    if planoCliente:
        context = {'response':"Cadastro no plano concluido"}
        return render(request, "cliente/index.html", context)
    else:
        context = {'response':"Não foi possivel cadastrar"}
        return render(request, "cliente/index.html", context)




def create_cliente():
    return HttpResponse("Cadastro do Cliente")

def update_cliente():
    return HttpResponse("Atualizar Cliente")

def delete_cliente():
    return HttpResponse("Deletar Cliente")