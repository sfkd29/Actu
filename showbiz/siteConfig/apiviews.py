from rest_framework import viewsets
from . import serializers,models


class ContactViewset(viewsets.ModelViewset):
    query=models.Contact.objects.all()
    serializer_class=serializers.ContactSerializer()


class BreakingViewset(viewsets.ModelViewset):
    query=models.Breaking.objects.all()
    serializer_class=serializers.BreakingSerializer()