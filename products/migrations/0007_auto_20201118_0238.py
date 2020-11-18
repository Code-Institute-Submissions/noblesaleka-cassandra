# Generated by Django 3.1.3 on 2020-11-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_allowed_memberships'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='allowed_memberships',
        ),
        migrations.AddField(
            model_name='product',
            name='allowed_memberships',
            field=models.CharField(blank=True, default='Free', max_length=10, null=True),
        ),
    ]