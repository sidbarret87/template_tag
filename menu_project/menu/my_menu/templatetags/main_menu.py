from django import template
from my_menu.models import *

register= template.Library()

@register.inclusion_tag('menu.html')
def draw_menu(menu_title):
    if menu_title=='main_menu':
        genres = Genre.objects.all()[:4]
        detectives = Books.objects.filter(genre__title='Детектив')
        mystics = Books.objects.filter(genre__title='Мистика')
        realistics = Books.objects.filter(genre__title='Реализм')
        actions = Books.objects.filter(genre__title='Боевик')
        return {"genres":genres,'detectives':detectives, 'mystics':mystics,
                'realistics':realistics, 'menu_title':menu_title, 'actions':actions}
    elif menu_title == 'sub_menu':
            genres = Genre.objects.all()[4:]
            fantasys = Books.objects.filter(genre__title='Фэнтези')
            fantastics = Books.objects.filter(genre__title='Фантастика')

            return {"genres": genres,  'menu_title': menu_title, 'fantasys':fantasys,
                   'fantastics':fantastics}
    else:
        return {'menu_title':f'{menu_title} - Такого меню не существует'}