# Generated by Django 4.1.2 on 2022-10-19 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0002_rename_id_business_business_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='business_id',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
    ]
