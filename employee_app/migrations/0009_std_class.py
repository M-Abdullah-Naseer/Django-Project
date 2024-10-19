# Generated by Django 4.2.11 on 2024-07-27 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0008_school_system'),
    ]

    operations = [
        migrations.CreateModel(
            name='std_class',
            fields=[
                ('main_id', models.AutoField(primary_key=True, serialize=False)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_app.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_app.student')),
            ],
        ),
    ]