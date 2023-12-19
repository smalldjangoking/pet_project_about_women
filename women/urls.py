from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('articls/<slug:art_slug>', views.articls, name='articl'),
    path('categories/<slug:cat_slug>', views.categories, name='catarticls'),
    path('tag/<slug:slug_tag>', views.tag_view_page, name='slugindex'),
]