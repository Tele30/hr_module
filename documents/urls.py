from django.urls import path

from documents import views
from documents.views import ContractCreateView, ContractListView, ContractUpdateView, HolidayRequestCreateView, \
    HolidayListView

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

    path('holiday_requests/new/', HolidayRequestCreateView.as_view(), name='create_holiday_request'),
    path('holiday_list/new/', HolidayListView.as_view(), name='holiday_request_list'),

]
