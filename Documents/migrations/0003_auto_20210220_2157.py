# Generated by Django 3.1.5 on 2021-02-20 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0002_auto_20210220_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='cantact',
            new_name='contact',
        ),
    ]