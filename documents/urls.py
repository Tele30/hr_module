from django.urls import path

from documents import views

urlpatterns = [
    path('create-employee/', views.EmployeeCreateView.as_view(), name='create_employee'),
    path('', views.HomeTemplateView.as_view(), name='home_page'),
    path('list_of_employee/', views.EmployeeListView.as_view(), name='list_of_employee'),
    path('update_employee/<int:pk>/', views.EmployeeUpdateView.as_view(), name='update_employee'),
    path('delete_employee/<int:pk>/', views.EmployeeDeleteView.as_view(), name='delete_employee'),
    path('details-employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='details_employee')

]
