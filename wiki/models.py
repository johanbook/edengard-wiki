from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    date_posted = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Country(Article):
    language = models.CharField(max_length=64)
    population = models.IntegerField(default=-1)
    religion = models.CharField(max_length=64)

    climate = models.TextField(default=None, blank=True, null=True)
    etymology = models.TextField(default=None, blank=True, null=True)
    history = models.TextField(default=None, blank=True, null=True)
    locations = models.TextField(default=None, blank=True, null=True)
    military = models.TextField(default=None, blank=True, null=True)
    rule = models.TextField(default=None, blank=True, null=True)
    other = models.TextField(default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'countries'


class City(Article):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL)

    history = models.TextField(default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'cities'


class Item(Article):
    pass


class Language(Article):
    language_root = models.CharField(max_length=64)

    grammar = models.TextField(default=None, blank=True, null=True)
    phrases = models.TextField(default=None, blank=True, null=True)


class Opus(Article):

    class Meta:
        verbose_name_plural = 'opuses'


class Person(Article):
    pass


class Religion(Article):
    belief = models.TextField(default=None, blank=True, null=True)
    history = models.TextField(default=None, blank=True, null=True)
    worship = models.TextField(default=None, blank=True, null=True)


class Specie(Article):
    culture = models.TextField(default=None, blank=True, null=True)
    physiology = models.TextField(default=None, blank=True, null=True)
    occurrence = models.TextField(default=None, blank=True, null=True)
