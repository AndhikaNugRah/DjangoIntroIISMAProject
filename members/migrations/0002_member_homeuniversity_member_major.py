# Generated by Django 5.1 on 2024-08-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='homeuniversity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='major',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
