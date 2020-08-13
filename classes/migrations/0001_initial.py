# Generated by Django 2.2.8 on 2020-08-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(choices=[('100L', '100L'), ('200L', '200L'), ('300L', '300L'), ('400L', '400L'), ('500L', '500L')], default='100L', max_length=45)),
                ('teacher_id', models.ManyToManyField(to='teachers.Teacher')),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
    ]
