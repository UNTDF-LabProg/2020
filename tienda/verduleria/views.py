from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        'titulo': 'gracias por visitar nuestra verdulería!',
    }
    return render(request, 'home.html', context)
