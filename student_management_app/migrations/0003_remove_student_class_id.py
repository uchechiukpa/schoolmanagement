# Generated by Django 2.2.8 on 2020-08-20 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_student_class_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='class_id',
        ),
    ]
