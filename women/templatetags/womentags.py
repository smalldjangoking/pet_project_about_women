from django import template
from django.db.models import Count

from ..models import Category, TagPost

register = template.Library()


@register.inclusion_tag('woman/tagmenu.html')
def leftmenu(cat_selected=0):
    tagmenu = Category.objects.annotate(res=Count('cat')).filter(res__gt=1)
    return {'tagmenu': tagmenu, 'cat_selected': cat_selected}


@register.inclusion_tag('woman/tagblock.html')
def lefttegsmenu():
    lefttagsmenu = TagPost.objects.annotate(res=Count('tags')).filter(res__gt=1)
    return {'tagsmenu': lefttagsmenu}
