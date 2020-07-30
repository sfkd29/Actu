from rest_framework import serializers
from . import models



class ContactSerializer(models.serializers):
    class Meta:
        model=models.Contact
        fields= "__all__"


class BreakingSerializer(models.serializers):
    class Meta:
        model=models.Breaking
        fields= "__all__"