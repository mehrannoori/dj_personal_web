# Generated by Django 5.0.7 on 2024-07-16 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('special_status', 'can edit post')]},
        ),
    ]
