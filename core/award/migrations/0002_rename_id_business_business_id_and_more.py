# Generated by Django 4.1.2 on 2022-10-19 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='id',
            new_name='business_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='business',
            new_name='business_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='id',
            new_name='review_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='user_id',
        ),
    ]