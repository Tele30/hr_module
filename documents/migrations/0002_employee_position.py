# Generated by Django 5.0.6 on 2024-05-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(default='manager', max_length=50),
            preserve_default=False,
        ),
    ]
