from django.shortcuts import render,HttpResponse,redirect
from .models import Emp
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    emps = Emp.objects.all()
    return render(request,'index.html',{'emps':emps})


def add_emp(request):
    try:
       if request.method =="POST":
        Emp_name = request.POST.get("name")
        Emp_id = request.POST.get("id")
        Emp_phone = request.POST.get("phone")
        Emp_addres = request.POST.get("address")
        Emp_working = request.POST.get("working")
        Emp_department = request.POST.get("department")

       e = Emp()
       e.name = Emp_name
       e.emp_id = Emp_id
       e.phone = Emp_phone
       e.addres = Emp_addres
       e.department = Emp_department
      
       if Emp_working == None:
           e.working =  False
       else:
           e.working = True
       e.save()
       return HttpResponseRedirect('/home/')
    except:
        pass
    
    return render(request,'add_emp.html')

def delete(request,emp_id):
   emp = Emp.objects.get(id=emp_id)
   emp.delete()
   return redirect('/home/')
