# Generated by Django 5.1.5 on 2025-02-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_message_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
