# Generated by Django 3.1.5 on 2021-02-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]