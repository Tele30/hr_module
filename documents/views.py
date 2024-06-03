from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView

from documents.forms import EmployeeForm, EmployeeUpdateForm, ContractForm, HolidayRequestForm, CertificateEmployeeForm
from documents.models import Employee, Contract, HolidayRequest, CertificateEmployee


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


# Contract

class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Contract'
        context['form_button_text'] = 'Create'
        return context


class ContractListView(ListView):
    model = Contract
    template_name = 'contract/contract_list.html'
    context_object_name = 'contracts'


class ContractUpdateView(LoginRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('contract_list')
    permission_requierd = 'contract.change_contract'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Contract'
        context['form_button_text'] = 'Update'
        return context


class ContractDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "contract/delete_contract.html"
    model = Contract
    success_url = reverse_lazy('contract_list')
    permission_requierd = 'contract.delete_contract'


class HolidayRequestCreateView(CreateView):
    model = HolidayRequest
    form_class = HolidayRequestForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'HolidayRequest'
        context['form_button_text'] = 'Holiday'
        return context

class HolidayRequestListView(ListView):
    model = HolidayRequest
    template_name = 'HolidayRequest/holiday_request_list.html'
    context_object_name = 'holiday_requests'

class HolidayRequestUpdateView(UpdateView):
    model = HolidayRequest
    form_class = HolidayRequestForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('holiday_request_list')

class HolidayRequestDeleteView(DeleteView):
    model = HolidayRequest
    form_class = HolidayRequestForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('holiday_request_list')


class CertificateEmployeeCreateView(CreateView):
    model = CertificateEmployee
    form_class = CertificateEmployee
    template_name = 'any_form.html'
    success_url = reverse_lazy('home_page')
    context_object_name = 'certificates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'CertificateEmployee'
        context['form_button_text'] = 'Certificate'
        return context


class CertificateEmployeeListView(ListView):
    model = CertificateEmployee
    template_name = 'CertificateEmployee/certificates_employee_list.html'
    context_object_name = 'holiday_requests'


class CertificateEmployeeUpdateView(UpdateView):
    model = CertificateEmployee
    fields = ['date', 'reason', 'employee']
    template_name = 'any_form.html'
    success_url = reverse_lazy('certificates_employee_list')


class CertificateEmployeeDeleteView(DeleteView):
    model = CertificateEmployee
    form_class = CertificateEmployeeForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('certificates_employee_list')