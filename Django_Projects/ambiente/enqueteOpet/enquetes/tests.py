import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Questao

class QuestaoModelTest(TestCase):
    def test_publicado_recentemente_com_questao_futura(self):
        time = timezone.now() + datetime.timedelta(days=30)
        questao_futura = Questao(data_publicacao =time)
        self.assertIs(questao_futura.publicado_recentemente(),False)

    def test_publicado_recentemente_com_questao_antiga(self):
        time = timezone.now() - datetime.timedelta(days=6)
        questao_antiga = Questao(data_publicacao =time)
        self.assertIs(questao_antiga.publicado_recentemente(),False)

    def test_publicado_recentemente_com_questao_recente(self):
        time = timezone.now() - datetime.timedelta(days=2)
        questao_recente = Questao(data_publicacao =time)
        self.assertIs(questao_recente.publicado_recentemente(),True)

# teste de views
def criar_questao(questao_texto,dias):
     time = timezone.now() - datetime.timedelta(days=dias)
     return Questao.objects.create(questao_texto=questao_texto,data_publicacao=time)

class QuestaoIndexViewTest(TestCase):
    def test_sem_questao(self):
        response = self.client.get(reverse('enquetes:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Sem questoes")
        self.assertQuerysetEqual(
            response.context['ultimas_questoes'],[]
        ) 

    '''def test_questao_passada(self):
            criar_questao(questao_texto="Questao passada.",dias=-30)
            response = self.client.get(reverse('enquetes:index'))
            self.assertQuerysetEqual(
                response.context['ultimas_questoes'],['<Questao: Questao passada.>']
            )'''
    


    '''def test_questao_futura(self):
            criar_questao(questao_texto="Questao Futura.",dias = 30)
            response = self.client.get(reverse('enquetes:index'))
            self.assertContains(response,"Sem questoes")
            self.assertQuerysetEqual(
                response.context['ultimas_questoes'],[]
            )  '''
   
   
    ''' def test_questao_futura_e_questao_passada(self):
        criar_questao(questao_texto="Questao passada.",dias=-30)
        criar_questao(questao_texto="Questao futura.",dias=30)
        response = self.client.get(reverse('enquetes:index'))
        self.assertQuerysetEqual(
            response.context['ultimas_questoes'],['<Questao: Questao passada.>']
        )
        '''
    '''def test_duas_questoes_passada(self):
            criar_questao("Questao 1",dias = -30)
            criar_questao("Questao 2",dias = -5)
            response = self.client.get(reverse('enquetes:index'))
            self.assertQuerysetEqual(
                response.context['ultimas_questoes'],['<Questao: Questao 2>','<Questao: Questao 1>']
            ) '''



'''class QuestaoIndexViewTest(TestCase):
    def test_questao_futura(self):
        questao_futura= criar_questao(questao_texto='Questao futura',dias=30)
        url =reverse('enquetes:detail',args=(questao_futura.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)
   
   
    def test_questao_passada(self):
        questao_passada= criar_questao(questao_texto='Questao passada',dias=-10)
        url =reverse('enquetes:detail',args=(questao_passada.id,))
        response = self.client.get(url)
        self.assertContains(response,questao_passada.questao_texto)'''




                      
