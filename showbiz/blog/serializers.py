from rest_framework import serializers
from . import models


class ReponseSerializer(models.serializers):
    class Meta:
        model=models.Reponse
        fields= "__all__"


class CommentaireSerializer(models.serializers):
    reponse= ReponseSerializer(many=True,required=False)
    class Meta:
        model=models.Commentaire
        fields= "__all__"


class ArticleSerializer(models.serializers):
    commentaires= CommentaireSerializer(many=True,required=False)
    class Meta:
        model=models.Article
        fields= "__all__"


class TagSerializer(models.serializers):
    articles=ArticleSerializer(many=True,required=False)
    class Meta:
        model=models.Tag
        fields= "__all__"


class CategorieSerializer(models.serializers):
    articles=ArticleSerializer(many=True,required=False)
    class Meta:
        model=models.Categorie
        fields= "__all__"





#class CommentaireSerializer(models.serializers):
#    class Meta:
#        model=models.Commentaire
#        fields= "__all__"