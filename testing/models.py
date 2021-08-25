from django.db import models


class Test(models.Model):
    otvet1 = models.CharField('ФИО', max_length=50)
    otvet2 = models.CharField('Ответ 2', max_length=5)
    otvet3 = models.CharField('Ответ 3', max_length=5)
    otvet4 = models.CharField('Ответ 4', max_length=5)
    otvet5 = models.CharField('Ответ 5', max_length=5)

    def __str__(self):
        return self.otvet1

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
