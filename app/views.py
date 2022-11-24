from django.shortcuts import render

# Create your views here.

def  condition(request):
    return render(request,'condition.html',context={'a':100,'b':2000,'c':300})
