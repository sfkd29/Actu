from django.contrib import admin
from django.urls import path, include
from . import views
from .apiviews import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('contact',ContactViewset)
router.register('breaking',BreakingViewset)

app_name = 'siteConfig'

urlpatterns = [
    path('', views.index, name='index'),
    path('apis/',include('siteConfig.apiurls'))
]