# Generated by Django 3.2.5 on 2022-04-23 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_crypto_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='img_height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='crypto',
            name='img_width',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='image',
            field=models.ImageField(height_field='img_height', upload_to='posters/', verbose_name='Изображение криптовалюты', width_field='img_width'),
        ),
    ]
