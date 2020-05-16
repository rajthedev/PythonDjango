from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h1> hello good morning </h1>')

def good_afternoon_view():
    return HttpResponse('<h1> hello good afternoon </h1>')

def good_evening_view():
    return HttpResponse('<h1> hello good evening </h1>')