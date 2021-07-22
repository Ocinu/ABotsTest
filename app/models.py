from django.db import models


class WikiPage(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    content = models.TextField(verbose_name='Контент', )
    current_version = models.PositiveIntegerField(verbose_name='Поточна версія', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сторінка'
        verbose_name_plural = 'Сторінки'
        ordering = ['current_version']
