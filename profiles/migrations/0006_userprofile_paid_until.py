# Generated by Django 3.1.3 on 2021-01-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_userprofile_paid_until'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='paid_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
