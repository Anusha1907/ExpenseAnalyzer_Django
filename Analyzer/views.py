from django.shortcuts import render
from django.http import HttpResponse
from Analyzer.models import user_profile, general_expenses, mandatory_expenses, debts
from django.db.models import Sum

# Create your views here.

def dashboard(request):
    foodData=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        food=general_expenses.objects.filter(date_time__month=i).filter(Email='nish0349@gmail.com').filter(category='3').aggregate(Sum('amount'))
        if food['amount__sum'] is not None:
            foodData[i-1]=food['amount__sum']
    return render(request,'examples/dashboard.html',{'food':foodData})

def user(request):
    user=user_profile.objects.filter(Email='nish0349@gmail.com')
    context={
    "userData" : user
    }
    return render(request,'examples/user.html',context)

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
    return render(request,'examples/login.html')
