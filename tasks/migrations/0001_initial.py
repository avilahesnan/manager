# Generated by Django 4.2.7 on 2023-11-09 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('term', models.DateTimeField()),
                ('is_completed', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
                ('cover', models.ImageField(upload_to='tasks/covers/%Y/%m/%d/')),
                ('days_to_alert', models.IntegerField(default=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default='Area Not Specified', on_delete=django.db.models.deletion.SET_DEFAULT, to='tasks.category')),
            ],
        ),
    ]