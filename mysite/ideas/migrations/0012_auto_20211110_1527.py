# Generated by Django 2.2 on 2021-11-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0011_auto_20211110_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='category_choice',
            field=models.CharField(blank=True, choices=[('Science', 'Science'), ('Technology', 'Technology'), ('Engineering', ' Engineering'), ('M', 'Mathematics')], max_length=30, null=True),
        ),
    ]