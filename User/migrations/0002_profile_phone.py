# Generated by Django 4.0.3 on 2022-06-01 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, default=None, max_length=10, null=True),
        ),
    ]