from django.db import models
from tinymce import HTMLField
import hashlib
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

# Create your models here.

class Tag(models.Model):
    """Model definition for Tag."""

    # TODO: Define fields here
    titre = models.CharField(max_length=255, unique=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        return str(self.titre)


class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    titre = models.CharField(max_length=255, unique=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return str(self.titre)


class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    tags = models.ManyToManyField(Tag, related_name='articles')
    titre = models.CharField(max_length=50)
    titre_slug = models.SlugField(editable=False, null=True, max_length=255)
    cover = models.ImageField(upload_to='articles')
    contenu = HTMLField('Content')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='articles')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return str(self.titre)

    def save(self , *args ,**kwargs ):
        """Save method for Article."""
        super(Article, self).save(*args, **kwargs)
        encoding_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(str(self.titre) + ' ' + str(encoding_id.hexdigest()))
        super(Article, self).save(*args, **kwargs)


class Commentaire(models.Model):
    """Model definition for Commentaire."""

    # TODO: Define fields here
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    nom = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField()
    message = models.TextField()
    

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return '{}  -  {}'.format(self.nom, self.date_add)



class Reponse(models.Model):
    """Model definition for Reponse."""

    # TODO: Define fields here
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name= 'reponse')
    nom = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField()
    message = models.TextField()
    

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


    class Meta:
        """Meta definition for Reponse."""

        verbose_name = 'Reponse'
        verbose_name_plural = 'Reponses'

    def __str__(self):
        """Unicode representation of Reponse."""
        return '{}  -  {}'.format(self.nom, self.date_add)

