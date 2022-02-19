from django.shortcuts import render
from Menu import views as menu

# Create your views here.
def index(request):
    context = menu.getmenu()
    return render(request, 'IceAndSpice/index.html', context=context)