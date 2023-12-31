import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField(verbose_name='Наименование Организации')),
                ('customer_address', models.TextField(verbose_name='Адрес')),
                ('customer_city', models.TextField(verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Описание Контрагента',
                'verbose_name_plural': 'Описание Контрагентов',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(verbose_name='Производитель')),
                ('model', models.TextField(verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Доступное оборудование',
                'verbose_name_plural': 'Доступные оборудования',
                'db_table': 'devices',
            },
        ),
        migrations.CreateModel(
            name='DeviceInField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.TextField(verbose_name='Серийный номер')),
                ('owner_status', models.TextField(verbose_name='Статус Принадлежности')),
                ('analyzer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='crm_system.device', verbose_name='Оборудование')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='crm_system.customer', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оборудование в полях',
                'verbose_name_plural': 'Оборудования в полях',
                'db_table': 'devices_in_fields',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_description', models.TextField(verbose_name='Описание')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_updated_dt', models.DateTimeField(blank=True, null=True, verbose_name='Последнее изменение')),
                ('order_status', models.TextField(choices=[('open', 'открыта'), ('closed', 'закрыта'), ('in progress', 'в работе'), ('need info', 'нужна информация')], verbose_name='Статус заявки')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='crm_system.deviceinfield', verbose_name='Оборудование')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'db_table': 'orders',
            },
        ),
    ]