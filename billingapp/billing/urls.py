from django.urls import path
from billing.views import *

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:id>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-retrieve-update-destroy'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:id>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy'),
    path('bills/', BillListCreateAPIView.as_view(), name='bill-list-create'),
    path('bills/<int:id>/', BillRetrieveUpdateDestroyAPIView.as_view(), name='bill-retrieve-update-destroy'),
    path('analytics/', AnalyticsAPIView.as_view(), name='analytics'),
]
