# Generated by Django 3.1 on 2020-11-26 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_blacklist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blacklist',
            old_name='blacklisting',
            new_name='user',
        ),
        migrations.CreateModel(
            name='FriendsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]