# Generated by Django 4.2 on 2023-07-15 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailinglogs',
            options={'verbose_name': 'Лог рассылки', 'verbose_name_plural': 'Логи рассылки'},
        ),
        migrations.AlterModelOptions(
            name='mailingsetting',
            options={'verbose_name': 'Настройка рассылки', 'verbose_name_plural': 'Настройки рассылки'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AddField(
            model_name='mailingsetting',
            name='head_message',
            field=models.OneToOneField(default="<built-in function id>+'сообщение'", max_length=150, on_delete=django.db.models.deletion.CASCADE, to='main.message', verbose_name='Тема сообщения'),
        ),
        migrations.AddField(
            model_name='mailingsetting',
            name='log_time',
            field=models.OneToOneField(default='<built-in function id>', on_delete=django.db.models.deletion.CASCADE, to='main.mailinglogs', verbose_name='Lата и время последней попытки'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='почта_пользователя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='почта_пользователя'),
        ),
        migrations.AlterField(
            model_name='mailinglogs',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='почта_пользователя'),
        ),
        migrations.AlterField(
            model_name='mailingsetting',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='почта_пользователя'),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='почта_пользователя'),
        ),
        migrations.AlterField(
            model_name='message',
            name='head_message',
            field=models.CharField(default="<built-in function id>+'сообщение'", max_length=150, verbose_name='Тема сообщения'),
        ),
    ]
