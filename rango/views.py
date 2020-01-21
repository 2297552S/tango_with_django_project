from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("<a href = '/rango/'>Rango says welcome to the about page</a>")