# Generated by Django 4.1.2 on 2022-11-17 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogP', '0013_alter_project_check_code_alter_project_live_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='stack',
            field=models.CharField(default='', max_length=200),
        ),
    ]
