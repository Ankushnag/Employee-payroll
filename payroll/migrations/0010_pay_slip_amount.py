# Generated by Django 3.1.4 on 2021-06-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0009_auto_20210614_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay_slip',
            name='amount',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
