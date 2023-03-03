from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок новости', max_length=100)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации новости')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'News'
