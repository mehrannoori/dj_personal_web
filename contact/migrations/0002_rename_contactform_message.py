# Generated by Django 5.0.7 on 2024-07-23 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='Message',
        ),
    ]
