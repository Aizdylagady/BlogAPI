# Generated by Django 3.1 on 2021-03-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210316_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(4, 'excellent'), (3, 'very good'), (2, 'good'), (1, 'bad')], default=0),
        ),
    ]
