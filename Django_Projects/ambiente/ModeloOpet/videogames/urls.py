from django.urls import path

from . import views
app_name = 'videogames'
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:videogame_id>/',views.detail,name="detail")
    ]