# Generated by Django 2.2.8 on 2020-08-31 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_studentgrade_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgrade',
            name='percentage',
            field=models.DecimalField(decimal_places=1, default=20.9, max_digits=8),
        ),
    ]
