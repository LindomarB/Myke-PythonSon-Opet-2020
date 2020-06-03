from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import VideoGame
from django.template import loader

# Create your views here. 

def index(request):
    all_videogames = VideoGame.objects.order_by('-pub_date')#[:2] limita a consulta
    #output = ', '.join([v.vg_name for v in all_videogames])
    #template = loader.get_template('videogames/index.html')
    context = {'all_videogames':all_videogames}
    #return HttpResponse(template.render(context,request))
    #return HttpResponse(output)
    return render(request,'videogames/index.html',context)
def detail(request,videogame_id):
    videogame = get_object_or_404(VideoGame,pk=videogame_id)
    return render(request,'videogames/detail.html',{'videogame':videogame}) 

    #o codigo abaixo e substituido pelo codigo acima com menos linhas 
    '''try:
        videogame = VideoGame.objects.get(pk=videogame_id)
    except VideoGame.DoesNotExist:
        raise Http404("Video game não existe!")
    return render(request,'videogames/detail.html',{'videogame':videogame})'''
    
   
    
    #return HttpResponse("Dados do video Game {0}".format(videogame_id))
