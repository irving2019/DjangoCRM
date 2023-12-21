from django.db import models
from datetime import datetime

class Device(models.Model):

    class Meta:
        db_table = 'devices'
        verbose_name = "Номенклатура"
        verbose_name_plural = "Доступные оборудования"

    manufacturer = models.TextField(verbose_name="Производитель")
    model = models.TextField(verbose_name="Модель")

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Customer(models.Model):

    class Meta:
        db_table = 'customers'
        verbose_name = "Описание Контрагента"
        verbose_name_plural = "Описание Контрагентов"

    customer_name = models.TextField(verbose_name="Наименование Организации")
    customer_address = models.TextField(verbose_name="Адрес")
    customer_city = models.TextField(verbose_name="Город")

    def __str__(self):
        return f'{self.customer_name} по адресу: {self.customer_address}'


class DeviceInField(models.Model):

    class Meta:
        db_table = 'devices_in_fields'
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудования в полях"

    serial_number = models.TextField(verbose_name="Серийный номер")
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name="Пользователь")
    analyzer = models.ForeignKey(Device, on_delete=models.RESTRICT, verbose_name="Оборудование")
    owner_status = models.TextField(verbose_name="Статус Принадлежности")


    def __str__(self):
        return f'{self.analyzer} с/н {self.serial_number} в {self.customer}'


class Order(models.Model):

    class Meta:
        db_table = 'orders'
        verbose_name = "Заявку"
        verbose_name_plural = "Заявки"

    statuses = (('open', 'открыта'),
                ('closed', 'закрыта'),
                ('in progress', 'в работе'),
                ('need info', 'нужна информация'))

    device = models.ForeignKey(DeviceInField, verbose_name="Оборудование", on_delete=models.RESTRICT)
    order_description = models.TextField(verbose_name="Описание")
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    last_updated_dt = models.DateTimeField(verbose_name="Последнее изменение", blank=True, null=True)
    order_status = models.TextField(verbose_name="Статус заявки", choices=statuses)

    def __str__(self):
        return f'Заявка №{self.id} для {self.device}'

    def save(self, *args, **kwargs):
        self.last_updated_dt = datetime.now()
        super().save(*args, **kwargs)