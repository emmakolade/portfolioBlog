# Generated by Django 4.1.2 on 2022-11-17 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogP', '0014_project_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='stack',
            field=models.CharField(max_length=200),
        ),
    ]