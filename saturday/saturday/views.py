from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.http import JsonResponse
def About_Page(request):
    return HttpResponse("<h1>About Page</h1>")

def shopping_cart(request):
    data = {
        'item1': 'apple',
        'item2': 'banana',
        'item3': 'orange',
    }
    return  JsonResponse(data)

def showing_html(request):
    return render(request, 'home.html')

def story_page(request):
    return render(request, 'story.html')