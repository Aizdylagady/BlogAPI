# Generated by Django 3.1 on 2021-03-11 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply',
            new_name='post_id',
        ),
    ]
