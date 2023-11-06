from django.shortcuts import render

# Create your views here.
def my_intro(request):
    return render(request,'my_intro.html')

def my_work(request):
    return render(request,'my_work.html')


