# Generated by Django 5.0.1 on 2024-01-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_rename_f_name_musician_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='instrument_type',
            field=models.CharField(choices=[('GUITAR', 'Guitar'), ('PIANO', 'Piano'), ('DRUM', 'Drum'), ('KEYBOARD', 'Keyboard'), ('VIOLIN', 'Violin')], default='Guitar', max_length=50),
        ),
    ]