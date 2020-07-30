from rest_framework import viewsets
from . import serializers,models

class CommentaireViewset(viewsets.ModelViewset):
    query=models.Commentaire.objects.all()
    serializer_class=serializers.CommentaireSerializer()


class ReponseViewset(viewsets.ModelViewset):
    query=models.Reponse.objects.all()
    serializer_class=serializers.ReponseSerializer()


class ArticleViewset(viewsets.ModelViewset):
    query=models.Article.objects.all()
    serializer_class=serializers.ArticleSerializer()


class TagViewset(viewsets.ModelViewset):
    query=models.Tag.objects.all()
    serializer_class=serializers.TagSerializer()


class CategorieViewset(viewsets.ModelViewset):
    query=models.Categorie.objects.all()
    serializer_class=serializers.CategorieSerializer()