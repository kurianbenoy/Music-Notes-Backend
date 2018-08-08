import random,time
from django.shortcuts import render
from django.http import HttpResponse
#from django
# Create your views here.

def tester(request):
    a = {1:'C',2:'D',3:'E',4:'F',5:'G',6:'H'}
    for i in range(10):
        selector = random.randint(1,6)
        time.sleep(5)
        return (HttpResponse(a[selector]))
