# Generated by Django 2.2 on 2021-11-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0010_auto_20211110_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='category_choice',
            field=models.CharField(blank=True, choices=[('S', 'science'), ('T ', 'technology'), ('E', 'Pyhsics'), ('M', 'Mathematics')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
