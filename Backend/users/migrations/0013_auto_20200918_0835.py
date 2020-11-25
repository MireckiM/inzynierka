# Generated by Django 3.1 on 2020-09-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200817_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='orientation',
        ),
        migrations.AddField(
            model_name='user',
            name='orientation',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]