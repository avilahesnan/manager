# Generated by Django 4.2.7 on 2023-11-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='term',
            field=models.DateField(),
        ),
    ]