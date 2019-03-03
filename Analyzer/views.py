from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from Analyzer.models import user_profile, general_expenses, mandatory_expenses, debts
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from Analyzer.forms import registerform,loginform
from django.urls import reverse
# Create your views here.

def dashboard(request):
    return render(request,'examples/dashboard.html')

def user(request):
    # user
    return render(request,'examples/user.html')

def summary(request):
    return render(request,'examples/summary.html')

def debts(request):
    return render(request,'examples/debts.html')

def mandatory(request):
    return render(request,'examples/mandatory.html')

def analyze(request):
    return render(request,'examples/analyze.html')

def notification(request):
    return render(request,'examples/notification.html')

def addExpense(request):
    return render(request,'examples/AddExpense.html')

def addMoney(request):
    return render(request,'examples/AddMoney.html')
    
def logout(request):
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method=="POST":
       form=registerform(request.POST)
       print(request.POST)
       print("hii")
       if form.is_valid():
           user=form.save()
           user.set_password(user.password)
           user.save()
           return render(request,'examples/dashboard.html')
       else:
           print(form.errors)
           error=form.errors
           return render(request,'examples/register.html',{'error':error})
    else:
        form=registerform()
        print(form)
    return render(request,'examples/register.html',{'form':form})

def login(request):
    context={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(password)
        user=authenticate(username=username,password=password)
        if user:
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            error="Invalid Credentials"
            return render(request,'examples/login.html',{'error':error})   
    else:
        form=loginform()
        print(form)
        return render(request,'examples/login.html',{'form':form})




        #     login(request,Email)
        #     if request.GET.get('next',None):
        #         return HttpResponseRedirect(request.GET['next'])
        #     return render(request,'examples/dashboard.html')
        # else:
        #     form=loginform()
        #     context['error']="Provided invalid Credentials"
        #     return render(request,"examples/login.html",context)
