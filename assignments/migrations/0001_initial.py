# Generated by Django 2.2.8 on 2020-08-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=45)),
                ('course_id', models.ManyToManyField(to='courses.Course')),
            ],
        ),
    ]