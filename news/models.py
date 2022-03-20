from django.db import models
from django.contrib.auth.models import User

class Articles (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    title = models.CharField('Название', max_length=80)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    data = models.DateTimeField ('Дата публикации')
    image = models.ImageField(blank=True, upload_to='img/')
    image_url = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

