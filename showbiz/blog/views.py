from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from . import models
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:

    pub = models.Article.objects.filter(status=True)
    paginator = Paginator(pub, 9)
    page = request.GET.get('page')
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        print('test')
        p = paginator.page(paginator.num_pages)

    data = {
        'public':models.Article.objects.filter(status=True).order_by('-date_add')[:9],
        'rand': random (models.Article.objects.filter(status=True))[:3],
        'pub':p,
        'range': range(1, p.paginator.num_pages+1)

    }
    return render(request,'pages/index.html',data)


def single_post(request: HttpRequest, titre_slug: str) -> HttpResponse:
    data = {

        'break':models.Breaking.objects.filter(status=True).order_by('-date_add')[:4],

    }
    return render(request,'pages/blog/single-post.html',data)

