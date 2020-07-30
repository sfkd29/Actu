from .apiviews import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('categorie',CategorieViewset)
router.register('tag',TagViewset)
router.register('article',ArticleViewset)
router.register('commentaire',CommentaireViewset)
router.register('reponse',ReponseViewset)

urlpatterns = [
     
]

urlpatterns += router.urls
