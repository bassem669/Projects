# Generated by Django 5.1.5 on 2025-02-02 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentre',
            name='message_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='home.message'),
        ),
    ]
