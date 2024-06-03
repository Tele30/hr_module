from django.urls import path

from documents import views
from documents.views import ContractCreateView, ContractListView, ContractUpdateView, HolidayRequestCreateView, \
    HolidayRequestListView, CertificateEmployeeCreateView


class CertificateEmployeeListView:
    pass


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home_page'),

    path('create-employee/', views.EmployeeCreateView.as_view(), name='create_employee'),
    path('list_of_employee/', views.EmployeeListView.as_view(), name='list_of_employee'),
    path('update_employee/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update_employee'),
    path('delete_employee/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('details-employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='details_employee'),

    path('create-contract', ContractCreateView.as_view(), name='create_contract'),
    path('contract_list/', ContractListView.as_view(), name='contract_list'),
    path('contract/update/<int:pk>/', ContractUpdateView.as_view(), name='update_contract'),
    path('delete_contract/<int:pk>/', views.ContractDeleteView.as_view(), name='delete_contract'),

    path('holiday_requests/', HolidayRequestCreateView.as_view(), name='create_holiday_request'),
    path('holiday_request_list/', HolidayRequestListView.as_view(), name='holiday_request_list'),
    path('holiday_request_update/<int:pk>/', HolidayRequestListView.as_view(), name='holiday_request_update'),
    path('holiday_request_delete/<int:pk>/', HolidayRequestListView.as_view(), name='holiday_request_delete'),

    path('certificates', CertificateEmployeeCreateView.as_view(), name='create_certificate'),
    path('certificates_employee_list/', CertificateEmployeeListView.as_view(), name='certificate_employee_list'),
    path('update_certificate/<int:pk>/', views.CertificateEmployeeUpdateView.as_view(), name='update_certificate'),
    path('delete_certificate/<int:pk>/', views.CertificateEmployeeDeleteView.as_view(), name='delete_certificate'),

]
