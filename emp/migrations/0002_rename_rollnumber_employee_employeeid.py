# Generated by Django 5.0.7 on 2024-07-15 11:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("emp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="rollnumber",
            new_name="employeeid",
        ),
    ]
