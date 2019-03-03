from django.contrib import admin
from Analyzer.models import user_profile,general_expenses,mandatory_expenses,debts,notifications

# Register your models here.
admin.site.register(user_profile)
admin.site.register(general_expenses)
admin.site.register(mandatory_expenses)
admin.site.register(debts)
admin.site.register(notifications)
