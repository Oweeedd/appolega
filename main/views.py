from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    context = {
        'title': 'Home',
        'content': 'This is the home page',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }

    return render(request,'main/index.html', context)


def about(request):
    return HttpResponse("About page")
