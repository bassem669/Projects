# Generated by Django 5.1.5 on 2025-02-02 19:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_message_date_pulblie_alter_message_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date_published',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
