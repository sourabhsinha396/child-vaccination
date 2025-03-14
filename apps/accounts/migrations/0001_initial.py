# Generated by Django 4.0 on 2022-01-08 08:58

import apps.accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, help_text='Description of Medical Staff', max_length=800, null=True)),
                ('aadhar', models.CharField(blank=True, max_length=12, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.accounts.models.get_file_path)),
                ('place', models.CharField(blank=True, max_length=200, null=True)),
                ('is_medical_staff', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
