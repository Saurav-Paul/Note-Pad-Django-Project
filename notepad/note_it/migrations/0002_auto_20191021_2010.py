# Generated by Django 2.2.6 on 2019-10-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_it', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]