from django.db import models


class Shipment(models.Model):
    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    Email = models.CharField('Email', max_length=50)
    school = models.CharField('Название школы и №', max_length=50)
    age = models.CharField('Возраст', max_length=50)
    grade = models.CharField('Класс', max_length=50)
    fio = models.CharField('ФИО родителя', max_length=50)
    number_fio = models.CharField('Телефон родителя', max_length=50)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

