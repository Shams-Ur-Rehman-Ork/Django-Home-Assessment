# Generated by Django 4.0.2 on 2022-02-20 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('hire_date', models.DateField()),
            ],
        ),
    ]
