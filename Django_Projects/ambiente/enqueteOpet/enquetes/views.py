from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.utils import timezone

from .models import Questao, Escolha
# Create your views here.
'''
def index(request):
    ultimas_questoes = Questao.objects.order_by('-data_publicacao')
    #output = '- -'.join(q.questao_texto for q in ultimas_questoes)
    context = {'ultimas_questoes':ultimas_questoes}
    return render(request,'enquetes/index.html',context)
    #return HttpResponse(output)
    

def detail(request,questao_id) :
   questao = get_object_or_404(Questao,pk=questao_id)
 
   return render(request,'enquetes/detail.html',{'questao':questao})

def results(request,questao_id) :
    questao = get_object_or_404(Questao,pk=questao_id)
    return render(request,'enquetes/results.html',{'questao':questao})'''

class IndexView(generic.ListView):
    template_name= 'enquetes/index.html'
    context_object_name= 'ultimas_questoes'

    def get_queryset(self):
        #return Questao.objects.order_by('-data_publicacao')[:5]
        return Questao.objects.filter(data_publicacao__lte=timezone.now()).order_by('-data_publicacao')[:5]
class DetailView(generic.DetailView) :
    model = Questao
    template_name = 'enquetes/detail.html'

    def get_queryset(self):
        return Questao.objects.filter(data_publicacao__lte= timezone.now())



class ResultsView(generic.DetailView) :
    model = Questao
    template_name = 'enquetes/results.html'

def vote(request,questao_id) :
    questao = get_object_or_404(Questao,pk=questao_id)
   
    try:
       escolha_selecionada =questao.escolha_set.get(pk=request.POST['escolha'])
    except(KeyError,Escolha.DoesNotExist):
        return render(request,'enquetes/detail.html',
        {
            'questao':questao,
            'error_message': "Voce nao selecionou uma opçao"
        })
    else:
        escolha_selecionada.votos += 1
        escolha_selecionada.save()
        return HttpResponseRedirect(reverse('enquetes:results',args=(questao.id,)))   