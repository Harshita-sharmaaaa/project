# Generated by Django 5.0.1 on 2024-02-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_rename_lastname_student_father_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='feedback',
            field=models.CharField(max_length=200),
        ),
    ]
