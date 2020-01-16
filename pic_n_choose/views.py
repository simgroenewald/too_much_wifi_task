from django.http import HttpResponse
from django.shortcuts import render

# Defines the homepage function which fires the homepage template
def homepage(request):
    return render(request, 'homepage.html')
