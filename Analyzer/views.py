from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from Analyzer.models import user_profile, general_expenses, mandatory_expenses, debts, User
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from Analyzer.forms import registerform,loginform,generalexpensesform
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your views here.



def dashboard(request):
    userr=User.objects.filter(username=request.session['username']);
    for i in userr:
        id=i.id
    foodData=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        food=general_expenses.objects.filter(date_time__month=i).filter(user_id=id).filter(category='1').aggregate(Sum('amount'))
        if food['amount__sum'] is not None:
            foodData[i-1]=food['amount__sum']
    travelData=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        travel=general_expenses.objects.filter(date_time__month=i).filter(user_id=id).filter(category='2').aggregate(Sum('amount'))
        if travel['amount__sum'] is not None:
            travelData[i-1]=travel['amount__sum']
    groceriesData=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        groceries=general_expenses.objects.filter(date_time__month=i).filter(user_id=id).filter(category='3').aggregate(Sum('amount'))
        if groceries['amount__sum'] is not None:
            groceriesData[i-1]=groceries['amount__sum']
    electronicsData=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        electronics=general_expenses.objects.filter(date_time__month=i).filter(user_id=id).filter(category='4').aggregate(Sum('amount'))
        if electronics['amount__sum'] is not None:
            electronicsData[i-1]=electronics['amount__sum']
    clothData=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        cloth=general_expenses.objects.filter(date_time__month=i).filter(user_id=id).filter(category='5').aggregate(Sum('amount'))
        if cloth['amount__sum'] is not None:
            clothData[i-1]=cloth['amount__sum']
    houseData=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        house=general_expenses.objects.filter(date_time__month=i).filter(user_id=id).filter(category='6').aggregate(Sum('amount'))
        if house['amount__sum'] is not None:
            houseData[i-1]=house['amount__sum']
    otherData=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        other=general_expenses.objects.filter(date_time__month=i).filter(user_id=id).filter(category='7').aggregate(Sum('amount'))
        if other['amount__sum'] is not None:
            otherData[i-1]=other['amount__sum']
    allExpense=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1,13):
        all=general_expenses.objects.filter(date_time__month=i).filter(user_id=id).aggregate(Sum('amount'))
        if all['amount__sum'] is not None:
            allExpense[i-1]=all['amount__sum']
    return render(request,'examples/dashboard.html',{'food':foodData, 'travel' : travelData , 'Groceries' : groceriesData , 'Electronics' : electronicsData , 'Clothing' : clothData , 'Household' : houseData , 'Other' : otherData, 'all' : allExpense})


def user(request):
    user=user_profile.objects.filter(Email='nish0349@gmail.com')
    context={
    "userData" : user
    }
    return render(request,'examples/user.html',context)

def summary(request):
    userr=User.objects.filter(username=request.session['username']);
    for i in userr:
        id=i.id
    Date_spentodrer=general_expenses.objects.filter(user_id=id).order_by('date_time')
    Amount_order=general_expenses.objects.filter(user_id=id).order_by('amount')
    Category_order=general_expenses.objects.filter(user_id=id).order_by('category')
    total= [0, 0, 0, 0, 0, 0,0,0,0,0]
    for i in range(0,9):
        for data in Category_order :
            if data.category==i:
                 total[i]=total[i]+data.amount

    summar_dict={'Date':Date_spentodrer,'amount':Amount_order,'category':Category_order,'total':total}
    return render(request,'examples/summary.html',context=summar_dict)

def debts(request):
    return render(request,'examples/debts.html')

def mandatory(request):
    return render(request,'examples/mandatory.html')

def analyze(request):
    return render(request,'examples/analyze.html')

def notification(request):
    return render(request,'examples/notification.html')

def addExpense(request):
    if request.method=="POST":
       form=generalexpensesform(request.POST)
       userr=User.objects.filter(username=request.session['username'])
       for u in userr:
           id=u.id
       if form.is_valid():
           user=form.save(commit=False)
           user.userid_id=id
           user.save()
           message="Successfully Added"
           form=generalexpensesform()
           return render(request,'examples/AddExpense.html',{'form':form,'message':message})
       else:
           print(form.errors)
           error=form.errors
           return render(request,'examples/AddExpense.html',{'error':error})
    else:
        form=generalexpensesform()
        print(form)
        return render(request,'examples/AddExpense.html',{'form':form})


    return render(request,'examples/AddExpense.html')

def addMoney(request):
    return render(request,'examples/AddMoney.html')

def logout_view(request):
    try:
        del request.session['username']
        print("hiudhdue")
    except Keyerror:
        pass
    return HttpResponseRedirect(reverse('login'))



def register(request):
    if request.method=="POST":
       form=registerform(request.POST)
       print(request.POST)
       if form.is_valid():
           user=form.save()
           # user.set_password(user.password)
           user.save()
           return HttpResponseRedirect(reverse('login'))
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
        print(username)
        print(password)
        user=User.objects.get(username=username,password=password)
        print(user)
        if user:
            print(user)
            request.session['username']=username
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
