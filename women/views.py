from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .forms import Addpostform
from .models import Category, Women, TagPost


class MainIndex(TemplateView):
    template_name = 'woman/index.html'

    extra_context = {
        'cat_selected': 0,
        'title': 'Главная Страница',
        'data': Women.published.all()
    }


#def articls(request, art_slug):
#    art_get = get_object_or_404(Women, slug=art_slug)
#    context = {
#        'title': art_get.title,
#        'content': art_get.content,
#        'art_all': art_get
#    }
#    return render(request, 'woman/articl.html', context=context)

class ArticlView(DetailView):
    model = Women
    template_name = 'woman/articl.html'
    slug_url_kwarg = 'art_slug'
    context_object_name = 'data'

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


class CategoriesView(ListView):
    template_name = 'woman/catgories.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = cat.name
        context["cat_selected"] = cat.pk
        return context


class TagView(ListView):
    template_name = 'woman/index.html'
    context_object_name = 'data'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(tag__slug=self.kwargs['slug_tag']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['slug_tag'])
        context['title'] = f'Тег: {tag.name}'
        context['cat_selected'] = 0
        return context

def addpost(request):
    if request.method == 'POST':
        form = Addpostform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            return render(request, 'woman/add_post.html', {'form': form})
    else:
        form = Addpostform()
        return render(request, 'woman/add_post.html', {'form': form})


def about(request):
    return render(request, 'woman/about.html')
