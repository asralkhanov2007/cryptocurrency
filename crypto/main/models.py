from tabnanny import verbose
from django.db import models

# Create your models here.
class Crypto(models.Model):
    name = models.CharField('Введите имя криптовалюты', max_length=20)
    slug = models.SlugField('*',max_length=20, unique=True)
    image = models.ImageField('Изображение криптовалюты', upload_to='posters/')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Криптовалюта'
        verbose_name_plural = 'Криптовалюты'