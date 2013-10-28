from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

def index(request):
    context = ''
    return render(request, 'pixelapp/home.html', context)
    #return HttpResponse("k")