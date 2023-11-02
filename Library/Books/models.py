from django.db import models

class Book(models.Model):
    title = models.CharField('nome',max_length=255)
    author = models.CharField('author', max_length=255)
    publication_year = models.IntegerField('publication_year')
    
    def __str__(self):
        return f"Nome: {self.title}, Author: {self.author}, Puplication year: {self.publication_year}"
        