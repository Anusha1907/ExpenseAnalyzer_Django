from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from Analyzer import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ExpenseAnalyzer/', include('django.contrib.auth.urls')),
    url(r'^$', views.login,name='login'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('register/', views.register, name='register'),
    path('user/',views.user,name='user'),
    path('Summary/',views.summary,name='summary'),
    path('debts/',views.debts,name='debts'),
    path('mandatory/',views.mandatory,name='mandatory'),
    path('analyze/',views.analyze,name='analyze'),
    path('notification/',views.notification,name='notification'),
    path('AddExpense/',views.addExpense,name='AddExpense'),
    path('AddMoney/',views.addMoney,name='AddMoney')


]
