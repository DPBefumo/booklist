# Generated by Django 3.0.7 on 2020-06-26 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200626_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('To_Read', 'To Read'), ('Reading', 'Reading'), ('Read', 'Read')], default='', max_length=10),
        ),
    ]