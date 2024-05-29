from django.contrib import admin
from .models import Employee, Contract, HolidayRequest, CertificateEmployee

admin.site.register(Employee)
admin.site.register(Contract)
admin.site.register(HolidayRequest)
admin.site.register(CertificateEmployee)

