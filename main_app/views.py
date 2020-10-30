from django.shortcuts import render, redirect
from django.http import HttpResponse



# ---------------- STATIC FILES
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')