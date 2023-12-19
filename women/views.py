from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Women, TagPost


def index(request):
    w_list = Women.objects.all()
    context = {
        'data': w_list,
        'cat_selected': 0,
        'title': 'Главная Страница'
    }
    return render(request, 'woman/index.html', context=context)


def articls(request, art_slug):
    art_get = get_object_or_404(Women, slug=art_slug)
    context = {
        'title': art_get.title,
        'content': art_get.content,
    }
    return render(request, 'woman/articl.html', context=context)


def categories(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=category.pk)


    context = {
        'posts': posts,
        'cat_selected': category.pk,
        'title': category
    }
    return render(request, 'woman/catgories.html', context=context)

def tag_view_page(request, slug_tag):
    tag = get_object_or_404(TagPost, slug=slug_tag)
    posts = tag.tags.filter(is_published=Women.Publisherdraft.PUBLISHED)

    data = {
        'data': posts,
        'cat_selected': 0,
        'title': f'Тег: {tag.name}',
    }
    return render(request, 'woman/index.html', context=data)
