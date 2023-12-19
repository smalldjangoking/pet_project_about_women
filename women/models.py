from django.db import models
from django.urls import reverse


class Women(models.Model):
    class Publisherdraft(models.IntegerChoices):
        DRAFT = 0, 'Не опубликовано'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=25)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Publisherdraft.choices, default=Publisherdraft.DRAFT)
    cat = models.ForeignKey(to='Category', on_delete=models.PROTECT)
    tag = models.ManyToManyField(to="TagPost", blank=True, related_name='tags')

    def get_absolute_url(self):
        return reverse('articl', kwargs={'art_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(unique=True, max_length=15, db_index=True)
    slug = models.SlugField(max_length=45, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catarticls', kwargs={'cat_slug': self.slug})

class TagPost(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=50)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('slugindex', kwargs={'slug_tag': self.slug})