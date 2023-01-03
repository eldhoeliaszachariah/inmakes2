from django.shortcuts import render
from django.shortcuts import render
def demo(request):
    return render(request,"index.html")