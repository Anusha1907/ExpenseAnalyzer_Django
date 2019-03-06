from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User,Group
from django.forms import ModelForm
from Analyzer.models import user_profile, general_expenses, mandatory_expenses, debts



class registerform(forms.ModelForm):

     password=forms.CharField(widget=forms.PasswordInput())
     
       

     class Meta:
        model = User
        fields=('email','last_name','first_name','username','password')

     # def clean_first_name(self):
     #    cleaned_data = self.cleaned_data
     #    first_name = cleaned_data.get('first_name')
     #    print(first_name)

     #    if not first_name.isalpha():
     #        raise forms.ValidationError('Please enter a real name.')
     #    elif first_name[0].isupper() == False or first_name[1:].isupper() == True:
     #        raise forms.ValidationError('Please capitalize properly')
     #    else:
     #        cleaned_data['first_name'] = first_name
     #        print("from forms")
     #        print(cleaned_data)


     #    return cleaned_data



     # def clean_last_name(self):
     #    cleaned_data = self.cleaned_data
     #    last_name = cleaned_data.get('last_name')

     #    if not last_name.isalpha():
     #        raise forms.ValidationError('Please enter a real name.')
     #    elif last_name[0].isupper() == False or last_name[1:].isupper() == True:
     #        raise forms.ValidationError('Please capitalize properly')
     #    else:
     #        cleaned_data['last_name'] = last_name
     #        print(cleaned_data)
     #    return cleaned_data
      

     # def clean_username(self):
     #    cleaned_data = self.cleaned_data
     #    username = cleaned_data.get('username')
     #    print(username)

     #    if not len(username)>=6:
     #        raise forms.ValidationError('Username is too short.')
     #    elif len(username)>=30:
     #        raise forms.ValidationError('Username is too long')
     #    else:
     #        cleaned_data['username'] = username

     #    return cleaned_data

     # def clean_password(self):
     #    cleaned_data = self.cleaned_data
     #    password = cleaned_data.get('password')

     #    if not len(password)>=6:
     #        raise forms.ValidationError('Password is too short.')
     #    elif len(password)>=30:
     #        raise forms.ValidationError('Password is too long')
     #    else:
     #        cleaned_data['password'] = password

     #    return cleaned_data       
  

class loginform(forms.ModelForm):

     password=forms.CharField(widget=forms.PasswordInput())
     class Meta:
     	model=User
     	fields=('username','password')

