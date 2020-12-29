# Generated by Django 3.1.3 on 2020-12-28 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='automatic',
            field=models.CharField(blank=True, default='N', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stripe_plan_id',
            field=models.CharField(blank=True, default='', max_length=1, null=True),
        ),
    ]
