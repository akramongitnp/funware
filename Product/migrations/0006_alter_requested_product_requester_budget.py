# Generated by Django 4.0.3 on 2022-06-16 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_requested_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requested_product',
            name='requester_budget',
            field=models.CharField(max_length=50),
        ),
    ]