from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request=request, template_name="index.html")

def bingo(request):
    return render(request, 'bingo.html')

def bmi(request):
    return render(request, "bmi.html")