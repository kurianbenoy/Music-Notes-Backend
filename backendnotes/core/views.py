import random,time,logging
from django.shortcuts import render
from django.http import HttpResponse
#from django
# Create your views here.

def shrinker(beats):
    return (0.7059*beats)



#
# def tester(request):
#     i = 0
#     notes = ["B","A","B","B","B","B","B","D","G","A","B","C","C","C","C","C","B","B","B"]
#     len(notes)
#     # logger = logging.getLogger()
#     # #Setting the threshold of logger to DEBUG
#     # logger.setLevel(logging.DEBUG)
#
#
#
#     while i<len(notes):
#         time.sleep(shrinker(1))
#         return (HttpResponse(notes[i]))
#         notes.pop(0)

def tester(request):
    notes = ['D','B','A','G','D','D','D','D','B','A','G','E','E','C','D','A','F','D','D','C','A','G','D','B','A','G','D','D','B','A','G','E','E','E','C','B','A','D','D','D','D','E','D','C','A','G','B','B','B','B','B','B','B','D','G','A','B','C','C','C','C','C','B','B','B','B','B',]
    # beats = [1,1,1,1,3,.5,.5,1,1,1,1,4,1,1,1,1,4,1,1,1,1,4,1,1,1,1,4,1,1,1,1,3,1,1,1,1,1,1,1,1,1,,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1]

    for i in range(10):
        selector = random.randint(1,67)
        time.sleep(shrinker(1))
        return (HttpResponse(notes[selector]))
