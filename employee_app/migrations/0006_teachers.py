# Generated by Django 4.2.11 on 2024-07-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0005_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_gender', models.CharField(max_length=100)),
            ],
        ),
    ]