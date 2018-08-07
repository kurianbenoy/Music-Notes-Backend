import random
from django.shortcuts import render
from django
# Create your views here.

def tester(request):
    a = {1:'C',2:'D',3:'E',4:'F',5:'G',6:'H'}
    selector = random.randint(1,6)
    return (HttpResponse(a[selector]))
