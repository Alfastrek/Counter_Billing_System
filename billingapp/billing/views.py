from rest_framework import generics
from .models import Employee, Product, Customer, Bill
from .serializers import EmployeeSerializer, ProductSerializer, CustomerSerializer, BillSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from django.db.models import Count, Sum

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]  

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id' 
    
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'  

class BillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'id' 

class AnalyticsAPIView(APIView):
    def get(self, request, format=None):
        # Get the employee who made the maximum sales
        max_sales_employee = Bill.objects.values('employee__id', 'employee__username').annotate(total_sales=Sum('total_amount')).order_by('-total_sales').first()
        
        # Get the product that sells the most
        max_sales_product = Bill.objects.values('products__id', 'products__name').annotate(total_sales=Sum('total_amount')).order_by('-total_sales').first()

        return Response({
            'max_sales_employee': max_sales_employee,
            'max_sales_product': max_sales_product
        })
    

