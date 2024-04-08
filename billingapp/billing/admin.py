from django.contrib import admin
from .models import Employee, Product, Customer, Bill

admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Bill)