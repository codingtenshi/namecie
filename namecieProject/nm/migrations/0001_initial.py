# Generated by Django 4.2.3 on 2023-08-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.CharField(blank=True, default=True, max_length=40, primary_key=True, serialize=False, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('full_name', models.CharField(blank=True, max_length=80, null=True)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('email', models.EmailField(blank=True, max_length=50, unique=True)),
            ],
        ),
    ]
