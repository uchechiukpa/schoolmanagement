# Generated by Django 2.2.8 on 2020-08-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentupload',
            name='student_name',
            field=models.CharField(default='musa', max_length=255),
        ),
    ]
