from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def employee_info_view(request):
    #employees = Employee.objects.all()
    #employees = Employee.objects.filter(esal__lt=11000)
    #employees = Employee.objects.filter(ename__startswith='A')
    employees = Employee.objects.all().order_by('esal')
    return render(request, 'testapp/results.html', {'employees':employees})
