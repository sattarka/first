from django.http import HttpResponse
from django.shortcuts import render
import operator


def first(request):
    return(render(request,'first.html',{'first':'Equanimity'}))

def count(request):
    full=request.GET['fulltext']
    a=full.split()

    b={}
    for t in a:
        if t in b:
            b[t]+=1
        else:
            b[t]=1
    c=sorted(b.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'text':full,'num':len(a),'dic':c})
