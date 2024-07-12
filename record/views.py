from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'view_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            salary = request.POST.get('salary')
            bonus = request.POST.get('bonus')
            phone = request.POST.get('phone')
            dept_id = request.POST.get('dept')
            role_id = request.POST.get('role')
            hire_date=request.POST.get('hire_date')

            # Retrieve department and role objects
            dept = Department.objects.get(pk=dept_id)
            role = Role.objects.get(pk=role_id)

            # Create new Employee object and save to database
            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                bonus=bonus,
                phone=phone,
                dept=dept,
                role=role,
                hire_date=hire_date
            )
            new_emp.save()
            return HttpResponse('Employee added successfully')
        except Exception as e:
            return HttpResponse(f'Error adding employee: {str(e)}')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('Invalid request method')



def delete_emp(request,emp_id=0):
    
    emp=Employee.objects.all()
    context={
        'emp':emp
    }
    if emp_id:
        try:
            emp_to_remove=Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("Employee removed successfully")
        except Employee.DoesNotExist:
            return HttpResponse("Please Enter a valid employee id")
    return render(request, 'delete_emp.html',context)




def filter_emp(request):
    if request.method=='POST':
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        role=request.POST.get('role')
        emp=Employee.objects.all()
        if name:
         emp=emp.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emp=emp.filter(dept__name__icontains=dept)
        if role:
            emp=emp.filter(role__name__icontains=role)
        context={
        'emp':emp,
        'name':name,
        'dept':dept,
        'role':role,
            }
        return render(request,'view_emp.html',context)
    
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
       return HttpResponse('An Exceptional occur ') 
    
     




    

    
    
