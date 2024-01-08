from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.MainIndex.as_view(), name='main_page'),
    path('articls/<slug:art_slug>', views.ArticlView.as_view(), name='articl'),
    path('categories/<slug:cat_slug>', views.CategoriesView.as_view(), name='catarticls'),
    path('tag/<slug:slug_tag>', views.TagView.as_view(), name='slugindex'),
    path('addpost', views.addpost, name='addpost'),
    path('about', views.about, name='aboutpage')
]

