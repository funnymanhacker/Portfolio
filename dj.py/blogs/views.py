from django.shortcuts import render,redirect 
from django.http  import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')
def old(request):
    return redirect("abi")
def abi(request):
    return HttpResponse("hello,i am happy to be there old")
def Home(request):
    return render(request, 'Home.html')
def authview(request):
    if request == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})
def about(request):
    return render(request,'About.html')

 