from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from Analyzer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ExpenseAnalyzer/', include('django.contrib.auth.urls')),
    url(r'^$', views.dashboard,name='dashboard'),
    path('user/',views.user,name='user'),
    path('Summary/',views.summary,name='summary'),
    path('debts/',views.debts,name='debts'),
    path('mandatory/',views.mandatory,name='mandatory'),
    path('analyze/',views.analyze,name='analyze'),
    path('notification/',views.notification,name='notification'),
    path('AddExpense/',views.addExpense,name='AddExpense'),
    path('AddMoney/',views.addMoney,name='AddMoney'),
    url(r'logout',views.logout,name='logout')

]
