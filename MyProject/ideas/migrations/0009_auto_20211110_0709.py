# Generated by Django 3.2.8 on 2021-11-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0008_auto_20211109_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='yourname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(blank=True, choices=[('none', 'None'), ('bd', 'programming'), ('sg ', 'mechanics'), ('hj', 'Pyhsics')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
