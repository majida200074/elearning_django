# Generated by Django 4.2 on 2023-05-05 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprentissage1', '0004_student_date_de_naissance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_de_naissance',
        ),
    ]
