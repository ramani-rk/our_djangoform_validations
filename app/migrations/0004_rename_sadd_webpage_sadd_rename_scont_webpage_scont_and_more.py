# Generated by Django 4.2.7 on 2024-01-09 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_webpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webpage',
            old_name='sadd',
            new_name='Sadd',
        ),
        migrations.RenameField(
            model_name='webpage',
            old_name='scont',
            new_name='Scont',
        ),
        migrations.RenameField(
            model_name='webpage',
            old_name='sname',
            new_name='Sname',
        ),
    ]
