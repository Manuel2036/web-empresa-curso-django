from django import template
from pages.models import Page


register = template.Library()

@register.simple_tag # transformamos una funcion normal en un tag simple y lo registramos en la libreria de tamplates 
def get_page_list():
    pages = Page.objects.all()
    return pages

