# Generated by Django 4.0.3 on 2022-07-05 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aesys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='name_id',
        ),
    ]
