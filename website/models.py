from django.db import models

LAIDY = 'Laidy Pérez'


class ToBePublished(models.Model):
    draft = models.BooleanField(default=True)
    author = models.CharField(max_length=100, default=LAIDY)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Poem(ToBePublished):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Frase(ToBePublished):

    def __str__(self):
        return self.content[:50] + '...'
