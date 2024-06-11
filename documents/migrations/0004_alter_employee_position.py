# Generated by Django 5.0.6 on 2024-06-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_rename_phone_number_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('employee', 'Employee'), ('hr', 'Human Resource'), ('manager', 'Manager')], max_length=50),
        ),
    ]
