from django import forms
from .models import Evento, Palestrante, Participante, Ingresso, Programacao

class EventoForm(forms.ModelForm):
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Remove o formato do widget
        input_formats=['%Y-%m-%d', '%d/%m/%Y']  # Aceita os dois formatos
    )

    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Remove o formato do widget
        input_formats=['%Y-%m-%d', '%d/%m/%Y']  # Aceita os dois formatos
    )


    class Meta:
        model = Evento
        fields = '__all__'

class PalestranteForm(forms.ModelForm):
    class Meta:
        model = Palestrante
        fields = ['nome', 'bio', 'contato', 'evento']
    evento = forms.ModelChoiceField(queryset=Evento.objects.all(), required=True)  # Campo para selecionar o evento

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'

class IngressoForm(forms.ModelForm):
    data_compra = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Remove o formato do widget
        input_formats=['%Y-%m-%d', '%d/%m/%Y']  # Aceita os dois formatos
    )

    class Meta:
        model = Ingresso
        fields = '__all__'

class ProgramacaoForm(forms.ModelForm):
    horario = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Usando o tipo datetime-local para input
        input_formats=['%d/%m/%Y %H:%M', '%Y-%m-%d %H:%M']  # Aceita os dois formatos
    )

    class Meta:
        model = Programacao
        fields = '__all__'
