# Generated by Django 2.1.5 on 2019-04-14 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190414_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='image',
        ),
    ]