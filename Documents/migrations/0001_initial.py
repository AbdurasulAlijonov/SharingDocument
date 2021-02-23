# Generated by Django 3.1.5 on 2021-02-20 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantact', models.CharField(max_length=50, null=True)),
                ('branch', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadingdate', models.DateField(auto_now_add=True)),
                ('branch', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('notesfile', models.FileField(null=True, upload_to='')),
                ('filetype', models.CharField(max_length=50, null=True)),
                ('description', models.FileField(max_length=200, null=True, upload_to='')),
                ('status', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]