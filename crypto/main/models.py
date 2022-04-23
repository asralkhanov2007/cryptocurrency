from locale import currency
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class Crypto(models.Model):
    name = models.CharField('Введите имя криптовалюты', max_length=20)
    slug = models.SlugField('*',max_length=20, unique=True)
    img_width = models.PositiveIntegerField(null=True)
    img_height = models.PositiveIntegerField(null=True)
    image = models.ImageField('Изображение криптовалюты', upload_to='posters/',height_field='img_height', width_field='img_width')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Криптовалюта'
        verbose_name_plural = 'Криптовалюты'

class CryptoValue(models.Model):
    currency = models.ForeignKey(Crypto,on_delete=models.CASCADE,related_name='crypto_currency')
    crypto_value = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name}"

class ExchangeCrypto(models.Model):
    currencies = models.ManyToManyField(CryptoValue, related_name='crypto_exchange')
    crypto_value = models.FloatField(default=0)

    def __str__(self):
        return f"{self.crypto_value}"

