from django.db import models
class Genre(models.Model):
    title=models.CharField(max_length=100, verbose_name='Жанры')
    class Meta:
        verbose_name_plural='Жанры'
        verbose_name = 'Жанр'
        ordering=['title',]
    def __str__(self):
        return self.title
class Author(models.Model):
    name=models.CharField(max_length=100, verbose_name='Писатель')
    genre = models.ForeignKey('Genre', null=True,on_delete=models.PROTECT, verbose_name='Жанр')
    class Meta:
        verbose_name_plural='Писатели'
        verbose_name = 'Писатель'
        ordering=['name',]
    def __str__(self):
        return self.name


class Books(models.Model):
    title=models.CharField(max_length=250, verbose_name='Книги')
    genre=models.ForeignKey('Genre', null=True,on_delete=models.PROTECT, verbose_name='Жанр')
    author=models.ForeignKey('Author', null=True,on_delete=models.PROTECT, verbose_name='Писатель')
    class Meta:
        verbose_name_plural='Книги'
        verbose_name = 'Книга'
        ordering=['title',]
# Create your models here.
