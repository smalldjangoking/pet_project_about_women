from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Publisherdraft.PUBLISHED)

class Women(models.Model):
    class Publisherdraft(models.IntegerChoices):
        DRAFT = 0, 'Не опубликовано'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=25, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(verbose_name='Контент')
    img_file = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, default=None, null=True, verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Publisherdraft.choices)),
                                       default=Publisherdraft.DRAFT, verbose_name='Статус')
    cat = models.ForeignKey(to='Category', on_delete=models.PROTECT, related_name='cat', verbose_name='Категории')
    tag = models.ManyToManyField(to="TagPost", blank=True, related_name='tags', verbose_name='Теги')

    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        verbose_name = 'Известные Женщины'
        verbose_name_plural = 'Известные Женщины'
        ordering = ['-time_created']


    def get_absolute_url(self):
        return reverse('articl', kwargs={'art_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(unique=True, max_length=15, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=45, unique=True, db_index=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
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