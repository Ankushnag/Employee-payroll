# Generated by Django 3.1.3 on 2021-05-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0007_auto_20210520_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay_slip',
            name='emp_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
