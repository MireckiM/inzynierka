# Generated by Django 3.1 on 2020-08-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200817_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='xd'),
        ),
    ]
