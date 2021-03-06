# Generated by Django 3.0.7 on 2020-06-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200626_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='title',
            new_name='book',
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Read', 'Read'), ('To_Read', 'To Read')], default='', max_length=10),
        ),
    ]
