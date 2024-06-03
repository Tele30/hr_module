from django import forms
from django.contrib.auth.forms import UserCreationForm

from documents.models import Employee, Contract, HolidayRequest, CertificateEmployee


class EmployeeForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'position']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your last name'})

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your phone number'})
        self.fields['position'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your position'})

        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password confirmation'})

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'position']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your last name'})
        # self.fields['username'].widget.attrs.update(
        #     {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your phone'})
        self.fields['position'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your position'})

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['salary', 'start_date', 'end_date', 'employee']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salary'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Salary'})
        # self.fields['start_date'].widget.attrs.update()
        # self.fields['end_date'].widget.attrs.update(
        #     {'type': 'date', 'class': 'form-control', 'placeholder': 'End Date (optional)'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control'})


class HolidayRequestForm(forms.ModelForm):
    class Meta:
        model = HolidayRequest
        fields = ['start_date', 'end_date', 'status', 'employee', 'replacement']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control'})
        self.fields['replacement'].widget.attrs.update({'class': 'form-control'})



class CertificateEmployeeForm(forms.ModelForm):
    class Meta:
        model = CertificateEmployee
        fields = ['date', 'reason', 'employee']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reason'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control'})
