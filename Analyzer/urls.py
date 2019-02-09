from django.conf.urls import url
from django.urls import path
from Analyzer import views

urlpatterns = [
    url(r'^$', views.dashboard,name='dashboard'),
    path('user/',views.user,name='user'),
    path('Summary/',views.summary,name='summary'),
    path('debts/',views.debts,name='debts'),
    path('mandatory/',views.mandatory,name='mandatory'),
    path('analyze/',views.analyze,name='analyze'),
    path('notification/',views.notification,name='notification'),
    path('AddExpense/',views.addExpense,name='AddExpense'),
    path('AddMoney/',views.addMoney,name='AddMoney')

]
