from django.shortcuts import render
from django.http import HttpResponse

# Create your views here..
def hello_world_view(request):
    return HttpResponse('<h1>This is simple Django Application</h1>')