import random,time
from django.shortcuts import render
from django.http import HttpResponse
#from django
# Create your views here.

void shrinker(beats):
    return (0.7059*beats)

def tester(request):
    a = {1:'C',2:'D',3:'E',4:'F',5:'G',6:'A',7:'B'}
    notes = ['D','B','A','G','D','D','D','D','B','A','G','E','E','C','D','A','F','D','D','C','A','G','D','B','A','G','D','D','B','A','G','E','E','E','C','B','A','D','D','D','D','E','D','C','A','G','B','B','B','B','B','B','B','D','G','A','B','C','C','C','C','C','B','B','B','B','B',]
    beats = [1,1,1,1,3,.5,.5,1,1,1,1,4,1,1,1,1,4,1,1,1,1,4,1,1,1,1,4,1,1,1,1,3,1,1,1,1,1,1,1,1,1,,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1]
    
    
    for i in range(10):
        selector = random.randint(1,6)
        time.sleep(5)
        return (HttpResponse(a[selector]))
