from django.shortcuts import render,redirect
from .forms import EmployeCreationForm,EmployeUpdateForm,DepartmentCreationForm,LoginForm,DepartmentUpdationForm
from .models import Employe,Department
from django.contrib.auth import authenticate,login,logout
from .decorators import signin_required
# Create your views here.

@signin_required
def emp_create(request,*args,**kwargs):
    context={}
    form=EmployeCreationForm()
    context["form"]=form
    if request.method == "POST":
        form = EmployeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addemployee")
    return render(request,"addemp.html",context)

@signin_required
def emp_view(request,*args,**kwargs):
    form = Employe.objects.all()
    context = {}
    context["form"] = form
    return render(request,"viewemp.html",context)

# @signin_required
def emp_remove(request,id,*args,**kwargs):
    employe = Employe.objects.get(id=id)
    employe.delete()
    return redirect("viewemployee")

# @signin_required
def emp_update(request,id,*args,**kwargs):
    employe = Employe.objects.get(id=id)
    form = EmployeCreationForm(instance=employe)
    context = {}
    context["form"]=form
    if request.method=="POST":
        form = EmployeCreationForm(instance=employe,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewemployee")
    return render(request,"empupdate.html",context)

# @signin_required
def emp_details(request,id,*args,**kwargs):
    employe = Employe.objects.get(id=id)
    context = {}
    context["employe"] = employe
    return render(request,"empdetails.html",context)

# @signin_required
def dep_details(request,id,*args,**kwargs):
    dep = Department.objects.get(id=id)
    context = {}
    context["dep"] = dep
    return render(request,"depdetails.html",context)

# @signin_required
def dep_update(request,id,*args,**kwargs):
    department = Department.objects.get(id=id)
    form = DepartmentCreationForm(instance=department)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form = DepartmentCreationForm(instance=department,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewdepartment")
    return render(request,"depupdate.html",context)

@signin_required
def dep_creation(request,*args,**kwargs):
    context = {}
    form = DepartmentCreationForm()
    context["form"] = form
    if request.method == "POST":
        form = DepartmentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("departmentadd")
    return render(request,"depadd.html",context)

@signin_required
def dep_view(request,*args,**kwargs):
    form = Department.objects.all()
    context = {}
    context["form"] = form
    return render(request,"viewdep.html",context)



# @signin_required
def dep_remove(request,id,*args,**kwargs):
    depu = Department.objects.get(id=id)
    depu.delete()
    return redirect("viewdepartment")


def signin(request):
    form = LoginForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("index")
            else:
                context = {}
                context["form"] = form
                return render(request, "login.html", context)
    return render(request,"login.html",context)

@signin_required
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("login")

@signin_required
def admin_index(request,*args,**kwargs):
    return render(request,"index.html")
