import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','db_conn.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
def populate(n):
    for i in range(100):
        feno=randint(1001,9999)
        fename=fake.name()
        fesal=randint(10000,20000)
        feaddr=fake.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,addr=feaddr)

populate(30)
