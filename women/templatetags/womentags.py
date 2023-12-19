from django import template
from ..models import Category, TagPost

register = template.Library()


@register.inclusion_tag('woman/tagmenu.html')
def leftmenu(cat_selected=0):
    tagmenu = Category.objects.all()
    return {'tagmenu': tagmenu, 'cat_selected': cat_selected}


@register.inclusion_tag('woman/tagblock.html')
def lefttegsmenu():
    lefttagsmenu = TagPost.objects.all()
    return {'tagsmenu': lefttagsmenu}
