# Generated by Django 5.1.1 on 2025-01-01 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_api', '0002_alter_internshipregistration_batch'),
        ('student', '0005_student_is_backlog_student_is_kt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshipacceptance',
            name='company',
        ),
        migrations.AddField(
            model_name='internshipacceptance',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='job_offer_acceptance', to='student.student'),
        ),
    ]
