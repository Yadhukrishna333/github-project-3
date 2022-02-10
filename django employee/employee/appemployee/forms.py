from cProfile import label
from .models import employee,empdetails
from django import forms

class formemployee(forms.Form):
    name=forms.CharField(max_length=100, label='Name')
    phone=forms.CharField(max_length=100, label='Phone')
    
class formempdetails(forms.Form):
    designation=forms.CharField(max_length=100, label='Desgn')
    salary=forms.CharField(max_length=100, label='Salary')
    #grosssalary=forms.CharField(max_length=100, label='Grosssalary')