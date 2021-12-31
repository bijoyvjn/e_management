from django import forms
from django.forms import ModelForm
from .models import Department,Employe


class EmployeCreationForm(ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"

        widgets = {
            "emp_no":forms.TextInput(attrs={'class':"form-control"}),
            "designation":forms.TextInput(attrs={'class':"form-control"}),
            "f_name":forms.TextInput(attrs={'class':"form-control"}),
            "l_name":forms.TextInput(attrs={'class':"form-control"}),
            "phone":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.EmailInput(attrs={'class':"form-control"}),
            "address_1":forms.TextInput(attrs={'class':"form-control"}),
            "address_2":forms.TextInput(attrs={'class':"form-control"}),
            "city":forms.TextInput(attrs={'class':"form-control"}),
            "state":forms.TextInput(attrs={'class':"form-control"}),
            "pin":forms.TextInput(attrs={'class':"form-control"}),
            "department":forms.Select(attrs={'class':"form-select"}),
        }

class EmployeUpdateForm(ModelForm):
    class Meta:
        model = Employe
        fields = "__all__"

        widgets = {
            "emp_no":forms.TextInput(attrs={'class':"form-control"}),
            "designation":forms.TextInput(attrs={'class':"form-control"}),
            "f_name":forms.TextInput(attrs={'class':"form-control"}),
            "l_name":forms.TextInput(attrs={'class':"form-control"}),
            "phone":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.EmailInput(attrs={'class':"form-control"}),
            "address_1":forms.TextInput(attrs={'class':"form-control"}),
            "address_2":forms.TextInput(attrs={'class':"form-control"}),
            "city":forms.TextInput(attrs={'class':"form-control"}),
            "state":forms.TextInput(attrs={'class':"form-control"}),
            "pin":forms.TextInput(attrs={'class':"form-control"}),
            "department":forms.Select(attrs={'class':"form-select"}),
        }

class DepartmentCreationForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

        widgets = {
            "dep_no":forms.TextInput(attrs={'class':'form-control'}),
            "name":forms.TextInput(attrs={'class':'form-control'}),
        }


class DepartmentUpdationForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

        widgets = {
            "dep_no":forms.TextInput(attrs={'class':'form-control'}),
            "name":forms.TextInput(attrs={'class':'form-control'}),
        }



class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))