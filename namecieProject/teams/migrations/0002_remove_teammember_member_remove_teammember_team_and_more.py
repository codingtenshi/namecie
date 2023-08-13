# Generated by Django 4.2.3 on 2023-08-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nm', '0002_alter_profile_image'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='member',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='team',
        ),
        migrations.RemoveField(
            model_name='teammoderator',
            name='moderator',
        ),
        migrations.RemoveField(
            model_name='teammoderator',
            name='team',
        ),
        migrations.AddField(
            model_name='team',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='teams_admin', to='nm.profile'),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='teams_member', to='nm.profile'),
        ),
        migrations.AddField(
            model_name='team',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='teams_moderator', to='nm.profile'),
        ),
        migrations.AddField(
            model_name='team',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='TeamAdmin',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.DeleteModel(
            name='TeamModerator',
        ),
    ]