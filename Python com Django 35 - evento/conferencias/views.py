from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Palestrante, Participante, Ingresso, Programacao
from .forms import EventoForm, PalestranteForm, ParticipanteForm, IngressoForm, ProgramacaoForm

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'conferencias/lista_eventos.html', {'eventos': eventos})

def criar_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'conferencias/form_evento.html', {'form': form})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'conferencias/form_evento.html', {'form': form})

def excluir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == "POST":
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'conferencias/confirmar_exclusao.html', {'objeto': evento})


def lista_palestrantes(request):
    palestrantes = Palestrante.objects.all()
    return render(request, 'conferencias/lista_palestrantes.html', {'palestrantes': palestrantes})

def criar_palestrante(request):
    if request.method == "POST":
        form = PalestranteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_palestrantes')
    else:
        form = PalestranteForm()
    return render(request, 'conferencias/form_palestrante.html', {'form': form})

def editar_palestrante(request, id):
    palestrante = get_object_or_404(Palestrante, id=id)
    if request.method == "POST":
        form = PalestranteForm(request.POST, instance=palestrante)
        if form.is_valid():
            form.save()
            return redirect('lista_palestrantes')
    else:
        form = PalestranteForm(instance=palestrante)
    return render(request, 'conferencias/form_palestrante.html', {'form': form})

def excluir_palestrante(request, id):
    palestrante = get_object_or_404(Palestrante, id=id)
    if request.method == "POST":
        palestrante.delete()
        return redirect('lista_palestrantes')
    return render(request, 'conferencias/confirmar_exclusao.html', {'objeto': palestrante})

def lista_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'conferencias/lista_participantes.html', {'participantes': participantes})

def criar_participante(request):
    if request.method == "POST":
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_participantes')
    else:
        form = ParticipanteForm()
    return render(request, 'conferencias/form_participante.html', {'form': form})

def editar_participante(request, id):
    participante = get_object_or_404(Participante, id=id)
    if request.method == "POST":
        form = ParticipanteForm(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            return redirect('lista_participantes')
    else:
        form = ParticipanteForm(instance=participante)
    return render(request, 'conferencias/form_participante.html', {'form': form})

def excluir_participante(request, id):
    participante = get_object_or_404(Participante, id=id)
    if request.method == "POST":
        participante.delete()
        return redirect('lista_participantes')
    return render(request, 'conferencias/confirmar_exclusao.html', {'objeto': participante})

def lista_ingressos(request):
    ingressos = Ingresso.objects.all()
    return render(request, 'conferencias/lista_ingressos.html', {'ingressos': ingressos})

def criar_ingresso(request):
    if request.method == "POST":
        form = IngressoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ingressos')
    else:
        form = IngressoForm()
    return render(request, 'conferencias/form_ingresso.html', {'form': form})

def editar_ingresso(request, id):
    ingresso = get_object_or_404(Ingresso, id=id)
    if request.method == "POST":
        form = IngressoForm(request.POST, instance=ingresso)
        if form.is_valid():
            form.save()
            return redirect('lista_ingressos')
    else:
        form = IngressoForm(instance=ingresso)
    return render(request, 'conferencias/form_ingresso.html', {'form': form})

def excluir_ingresso(request, id):
    ingresso = get_object_or_404(Ingresso, id=id)
    if request.method == "POST":
        ingresso.delete()
        return redirect('lista_ingressos')
    return render(request, 'conferencias/confirmar_exclusao.html', {'objeto': ingresso})

def lista_programacao(request):
    programacoes = Programacao.objects.all()
    return render(request, 'conferencias/lista_programacao.html', {'programacoes': programacoes})

def criar_programacao(request):
    if request.method == "POST":
        form = ProgramacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_programacao')
    else:
        form = ProgramacaoForm()
    return render(request, 'conferencias/form_programacao.html', {'form': form})

def editar_programacao(request, id):
    programacao = get_object_or_404(Programacao, id=id)
    if request.method == "POST":
        form = ProgramacaoForm(request.POST, instance=programacao)
        if form.is_valid():
            form.save()
            return redirect('lista_programacao')
    else:
        form = ProgramacaoForm(instance=programacao)
    return render(request, 'conferencias/form_programacao.html', {'form': form})

def excluir_programacao(request, id):
    programacao = get_object_or_404(Programacao, id=id)
    if request.method == "POST":
        programacao.delete()
        return redirect('lista_programacao')
    return render(request, 'conferencias/confirmar_exclusao.html', {'objeto': programacao})
