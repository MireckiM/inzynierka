# Generated by Django 3.0.5 on 2020-04-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(default='NONE', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='NONE', max_length=20),
        ),
    ]
