from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

# Create your models here.

class Contact(models.Model):
    """Model definition for Contact."""

    # TODO: Define fields here

    nom = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField()
    message = models.TextField()
    

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.nom


class Breaking(models.Model):
    """Model definition for Breaking."""

    # TODO: Define fields here
    heure = models.CharField( null=True, blank=True, max_length=50)
    annonce = models.CharField(max_length=50,null=True, blank=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Breaking."""

        verbose_name = 'Breaking'
        verbose_name_plural = 'Breakings'

    def __str__(self):
        """Unicode representation of Breaking."""
        return self.annonce

