from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView

from documents.forms import EmployeeForm, EmployeeUpdateForm
from documents.models import Employee


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


class EmployeeCreateView(CreateView):
    template_name = 'Employee/create_employee.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('home_page')


class EmployeeListView(LoginRequiredMixin, ListView):
    template_name = 'Employee/list_of_employee.html'
    model = Employee
    context_object_name = 'all_employee'
    permission_required = 'employee'


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'employee/update_employee.html'
    model = Employee
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('list_of_employee')
    permission_requierd = 'employee.change_employee'


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "employee/delete_employee.html"
    model = Employee
    success_url = reverse_lazy('list_of_employee')
    permission_requierd = 'employee.delete_employee'


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'employee/details_employee.html'
    model = Employee
    permission_requierd = 'employee.view_employee'