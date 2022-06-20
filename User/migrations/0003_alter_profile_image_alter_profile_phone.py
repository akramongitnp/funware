# Generated by Django 4.0.3 on 2022-06-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='http://bootdey.com/img/Content/avatar/avatar1.png', upload_to='assets/profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]