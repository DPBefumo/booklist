# Generated by Django 3.0.7 on 2020-06-26 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('To_Read', 'To_Read'), ('Reading', 'Reading')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('note', models.TextField(max_length=1000)),
                ('page_number', models.CharField(max_length=5)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='api.Book')),
            ],
        ),
    ]