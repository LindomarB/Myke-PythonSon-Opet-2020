from django.db import models
from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class VideoGame(models.Model):
    vg_name = models.CharField('Nome do produto:',max_length = 200)
    pub_date = models.DateTimeField('Publicado em:')
    vg_year =models.IntegerField('Ano de lançamento')
    vg_fab = models.CharField('Fabricante:',max_length=200, default='nome fabricante')
    vg_ativo = models.BooleanField('Ainda e vendido:', default=False)
    if vg_ativo == False:
        vg_ativo = 'Não'
    else:
        vg_ativo = 'Sim'    
    def __str__(self):
        return self.vg_name


    def foi_publicado_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    