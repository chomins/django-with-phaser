from django.shortcuts import render

# Create your views here.

def show(request): 
    return render(request, 'game.html')

def test(request): 
    return render(request, 'test.html')