from django.shortcuts import render

# Create your views here.
def web(request):
    d={'a':300 , 'b':200}
    return render(request,'web.html',context=d)