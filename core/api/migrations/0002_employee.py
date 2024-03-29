# Generated by Django 5.0.1 on 2024-01-16 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=50)),
                ('Employee_Email', models.CharField(max_length=20)),
                ('Employee_Address', models.CharField(max_length=200)),
                ('Employee_phone', models.CharField(max_length=20)),
                ('Employee_Position', models.CharField(choices=[('Manager', 'Manager'), ('Software Dev', 'Developer'), ('HR', 'HR')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
