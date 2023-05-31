from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':3000 , 'b':20000, 'c':400000}
    return render(request,'conditional.html',context=d)
def loops(request):
    d1={'name':'akash'}
    return render (request,'loops.html',d1)