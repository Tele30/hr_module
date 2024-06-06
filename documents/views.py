from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordContextMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView

from documents.forms import EmployeeForm, EmployeeUpdateForm, ContractForm, HolidayRequestForm, CertificateEmployeeForm
from documents.models import Employee, Contract, HolidayRequest, CertificateEmployee


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


class EmployeeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'Employee/create_employee.html'
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('home_page')

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser


class EmployeeListView(LoginRequiredMixin, ListView):
    template_name = 'Employee/list_of_employee.html'
    model = Employee
    context_object_name = 'all_employee'
    permission_required = 'employee'



class EmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'employee/update_employee.html'
    model = Employee
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('list_of_employee')
    permission_requierd = 'employee.change_employee'

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser


class EmployeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "employee/delete_employee.html"
    model = Employee
    success_url = reverse_lazy('list_of_employee')

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser


class EmployeeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'employee/details_employee.html'
    model = Employee

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser

# Contract

class ContractCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('home_page')

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Contract'
        context['form_button_text'] = 'Create'
        return context




class ContractListView(LoginRequiredMixin, ListView):
    model = Contract
    template_name = 'contract/contract_list.html'
    context_object_name = 'contracts'

    def get_queryset(self):
        # Angajații din HR sau superuserii pot vedea toate c
        if self.request.user.position == 'hr' or self.request.user.is_superuser:
            return CertificateEmployee.objects.all()
        # Angajații obișnuiți pot vedea doar propriile certificate
        return CertificateEmployee.objects.filter(employee=self.request.user)









class ContractUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('contract_list')
    permission_requierd = 'contract.change_contract'

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Contract'
        context['form_button_text'] = 'Update'
        return context


class ContractDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "contract/delete_contract.html"
    model = Contract
    success_url = reverse_lazy('contract_list')
    permission_requierd = 'contract.delete_contract'

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser

# AICI am lasat liber si nu am pus inca pentru ca ma gandesc la faptul ca fiecare angajat ar trebui /
# sa isi poata face in dreptul lui cerere

class HolidayRequestCreateView(LoginRequiredMixin, CreateView):
    model = HolidayRequest
    form_class = HolidayRequestForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'HolidayRequest'
        context['form_button_text'] = 'Holiday'
        return context


class HolidayRequestListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = HolidayRequest
    template_name = 'HolidayRequest/holiday_request_list.html'
    context_object_name = 'holiday_requests'

    def test_func(self):
        # todo as simple employee i should be able to see my own holiday request
        if self.request.user.position == 'manager' or self.request.user.is_superuser:
            return True
            # Angajații obișnuiți pot vedea doar propriile holiday requests
        return self.request.user.position == 'employee'
    def get_queryset(self):
        # Angajații tip Manager sau superuserii pot vedea toate holiday requests
        if self.request.user.position == 'manager' or self.request.user.is_superuser:
            return HolidayRequest.objects.all()
        # Angajații obișnuiți pot vedea doar propriile certificate
        return HolidayRequest.objects.filter(employee=self.request.user)


class HolidayRequestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = HolidayRequest
    form_class = HolidayRequestForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('holiday_request_list')

    def test_func(self):
        return self.request.user.position == 'manager' or self.request.user.is_superuser or self.request.user == self.object.employee

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'HolidayRequest'
        context['form_button_text'] = 'Update'
        return context


class HolidayRequestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = HolidayRequest
    form_class = HolidayRequestForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('holiday_request_list')

    def test_func(self):
        return self.request.user.position == 'manager' or self.request.user.is_superuser or self.request.user == self.object.employee


class CertificateEmployeeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CertificateEmployee
    form_class = CertificateEmployeeForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('home_page')
    context_object_name = 'certificates'

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Certificate Employee'
        context['form_button_text'] = 'Create Certificate'
        return context


class CertificateEmployeeListView(LoginRequiredMixin, ListView):
    model = CertificateEmployee
    template_name = 'CertificateEmployee/certificates_employee_list.html'
    context_object_name = 'certificates'


    def get_queryset(self):
        # Angajații din HR sau superuserii pot vedea toate certificatele
        if self.request.user.position == 'hr' or self.request.user.is_superuser:
            return CertificateEmployee.objects.all()
        # Angajații obișnuiți pot vedea doar propriile certificate
        return CertificateEmployee.objects.filter(employee=self.request.user)




class CertificateEmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CertificateEmployee
    form_class = CertificateEmployeeForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('certificates_employee_list')

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Certificate Employee'
        context['form_button_text'] = 'Update Certificate'
        return context


class CertificateEmployeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CertificateEmployee
    # form_class = CertificateEmployeeForm
    template_name = 'any_form.html'
    success_url = reverse_lazy('certificates_employee_list')

    def test_func(self):
        return self.request.user.position == 'hr' or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Certificate Employee'
        context['form_button_text'] = 'Delete Certificate'
        return context


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "registration/password_change_done.html"
    title = ("Password change successful")

