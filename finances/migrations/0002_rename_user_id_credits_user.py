# Generated by Django 3.2.3 on 2021-05-19 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credits',
            old_name='user_id',
            new_name='user',
        ),
    ]