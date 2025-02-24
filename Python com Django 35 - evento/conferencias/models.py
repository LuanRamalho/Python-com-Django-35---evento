from django.db import models

class Evento(models.Model):
	nome = models.CharField(max_length=200)
	descricao = models.TextField()
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	local = models.CharField(max_length=255)
	capacidade = models.IntegerField()

	def __str__(self):
		return self.nome

class Palestrante(models.Model):
	nome = models.CharField(max_length=200)
	bio = models.TextField()
	contato = models.EmailField()
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='palestrantes')

	def __str__(self):
		return self.nome

class Participante(models.Model):
	nome = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
	telefone = models.CharField(max_length=15)
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')

	def __str__(self):
		return self.nome

class Ingresso(models.Model):
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='ingressos')
	participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
	data_compra = models.DateTimeField(auto_now_add=True)

	tipo = models.CharField(max_length=100)  
	preco = models.DecimalField(max_digits=10, decimal_places=2)  

	def __str__(self):
		return f'{self.participante.nome} - {self.evento.nome}'

class Programacao(models.Model):
	horario = models.DateTimeField()
	palestrante = models.ForeignKey(Palestrante, on_delete=models.CASCADE, related_name='programacoes')
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='programacoes')

	def __str__(self):
		return f'{self.palestrante.nome} - {self.evento.nome} - ({self.horario})'
