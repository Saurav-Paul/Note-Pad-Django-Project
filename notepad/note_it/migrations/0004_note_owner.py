# Generated by Django 2.2.6 on 2019-10-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_it', '0003_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='owner',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]