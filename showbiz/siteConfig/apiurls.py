from .apiviews import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('contact',ContactViewset)
router.register('breaking',BreakingViewset)

urlpatterns = [
     
]

urlpatterns += router.urls
