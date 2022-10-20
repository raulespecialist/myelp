# Generated by Django 4.1.2 on 2022-10-20 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0005_rename_business_review_business_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='business_id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user_id',
        ),
        migrations.AddField(
            model_name='review',
            name='business',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='award.business'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='award.user'),
        ),
    ]
