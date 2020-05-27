from django.contrib import admin
from testapp.models import Employee


# Register your models here.
#admin.site.register(Employee)


#to display entire table in admin we need to below steps
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)