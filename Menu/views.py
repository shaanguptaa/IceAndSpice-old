from django.shortcuts import render
from Menu.models import Menu
# Create your views here.
# def menu(request):
#     context = {
#         'menu': {
#             'main': Menu.objects.filter(category__iexact='Main'),
#             'drinks': Menu.objects.filter(category__iexact='Drinks'),
#             'dessert': Menu.objects.filter(category__iexact='Dessert')
#         },
#         'state': "done"
#     }

#     return render(request, 'Menu/menu.html', context=context)

def getmenu(category=[]):
    data = {
        'menu': {
            'main': [item for item in Menu.objects.filter(category='Main').values()] or None,
            'drinks': [x for x in Menu.objects.filter(category__iexact='Drinks').values()] or None,
            'dessert': Menu.objects.filter(category__iexact='Dessert') or None,
        },
    }

    return data