# Generated by Django 2.2 on 2021-11-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0012_auto_20211110_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='category_choice',
            field=models.CharField(blank=True, choices=[('Science', 'Science'), ('Technology', 'Technology'), ('Engineering', ' Engineering'), ('Mathematics', 'Mathematics')], max_length=30, null=True),
        ),
    ]
