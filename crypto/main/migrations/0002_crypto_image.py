# Generated by Django 3.2.5 on 2022-04-22 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='image',
            field=models.ImageField(default=datetime.datetime(2022, 4, 22, 9, 35, 16, 259538, tzinfo=utc), upload_to='posters/', verbose_name='Изображение криптовалюты'),
            preserve_default=False,
        ),
    ]
