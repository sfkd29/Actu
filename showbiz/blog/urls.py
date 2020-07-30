from django.contrib import admin
from django.urls import path, include
from . import views
from .apiviews import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('categorie',CategorieViewset)
router.register('tag',TagViewset)
router.register('article',ArticleViewset)
router.register('commentaire',CommentaireViewset)
router.register('reponse',ReponseViewset)

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:titre_slug>/',views.single_post, name='singpost'),
    path('api/',include('blog.apiurls'))
    path('fap/', views.fap, name='fap')
]