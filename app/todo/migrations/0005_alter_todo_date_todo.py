# Generated by Django 4.0.6 on 2022-08-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_date_todo_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_todo',
            field=models.DateField(),
        ),
    ]