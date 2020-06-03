import datetime
from django.db import models
from django.db import models
from django.utils import timezone
# Create your models here.
class Questao(models.Model):
    questao_texto = models.CharField("Texto da Questão",max_length=200)
    data_publicacao = models.DateTimeField('Data da publicaçao')
    def publicado_recentemente(self):
        hoje =timezone.now()
        return hoje  - datetime.timedelta(days=4) <= self.data_publicacao <= hoje
    publicado_recentemente.admin_short_field = 'data_publicacao'
    publicado_recentemente.boolean =True
    publicado_recentemente.short_description ='Foi Publicado Recentemente?'




    def __str__(self):
        return self.questao_texto
class Escolha(models.Model):
    questao = models.ForeignKey(Questao,on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_length = 200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.escolha_texto



