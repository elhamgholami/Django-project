# Generated by Django 2.2 on 2021-11-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0013_auto_20211110_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='yourage',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
