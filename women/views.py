from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .forms import Addpostform
from .mixins import DataMixin
from .models import Category, Women, TagPost


class MainIndex(DataMixin, ListView):
    template_name = 'woman/index.html'
    title_context = 'Главная Страница'
    context_object_name = 'data'
    paginate_by = 3
    def get_queryset(self):
        return Women.published.all().select_related('cat')


class ArticlView(DetailView):
    model = Women
    template_name = 'woman/articl.html'
    slug_url_kwarg = 'art_slug'
    context_object_name = 'data'

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


class CategoriesView(DataMixin, ListView):
    template_name = 'woman/catgories.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context, title=cat.name, cat_selected=cat.pk)


class TagView(DataMixin, ListView):
    template_name = 'woman/index.html'
    context_object_name = 'data'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(tag__slug=self.kwargs['slug_tag']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['slug_tag'])
        return self.get_mixin_context(context, title=f'Тег: {tag.name}')


class AddPost(DataMixin, FormView):
    form_class = Addpostform
    template_name = 'woman/add_post.html'
    success_url = reverse_lazy('main_page')
    title_context = 'Добавление Статьи'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def about(request):
    return render(request, 'woman/about.html')
