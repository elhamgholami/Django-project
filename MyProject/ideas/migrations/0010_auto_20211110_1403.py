# Generated by Django 2.2 on 2021-11-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0009_auto_20211110_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(blank=True, choices=[('S', 'science'), ('T ', 'technology'), ('E', 'Pyhsics'), ('M', 'Mathematics')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
