# Generated by Django 2.2.8 on 2020-08-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annoucement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annoucements_title', models.CharField(max_length=45)),
                ('Annoucements_description', models.CharField(max_length=45)),
            ],
        ),
    ]
