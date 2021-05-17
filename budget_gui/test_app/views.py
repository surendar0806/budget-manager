from django.shortcuts import render

# Create your views here.
def index(request):
    return(render(request,'test_app/index.html'))

def relative(request):
    return(render(request,'test_app/rel_url_tem.html'))

def other(request):
    return(render(request,'test_app/other.html'))
