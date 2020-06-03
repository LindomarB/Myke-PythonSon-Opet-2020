from django.contrib import admin
from .models import Questao,Escolha

# Register your models here.

class EscolhaInLine(admin.TabularInline):
    model = Escolha
    extra = 3



class QuestaoAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Dados da Questao', {'fields':['questao_texto']}),
        ('informaçoes de data',{'fields':['data_publicacao'],'classes':['collapse']})
    ]
    inlines = [EscolhaInLine]
    list_display = ('questao_texto','data_publicacao','publicado_recentemente')
    list_filter =['data_publicacao']
    search_fields = ['questao_texto']
    #fields = ['data_publicacao','questai_texto']



admin.site.register(Questao,QuestaoAdmin)
#admin.site.register(Escolha)

 