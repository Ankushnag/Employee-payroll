# Generated by Django 3.1.4 on 2021-06-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0011_auto_20210614_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_personal_info',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='emp_photo'),
        ),
    ]