# Generated by Django 3.0.7 on 2020-06-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200626_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('Reading', 'Reading'), ('To_Read', 'To Read')], default='', max_length=10),
        ),
    ]
