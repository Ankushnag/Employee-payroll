# Generated by Django 3.1.4 on 2021-05-20 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0006_employee_connection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay_slip',
            name='amount',
        ),
        migrations.AddField(
            model_name='pay_slip',
            name='HRA',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pay_slip',
            name='basic_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pay_slip',
            name='other_allow',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pay_slip',
            name='total_earninig',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
