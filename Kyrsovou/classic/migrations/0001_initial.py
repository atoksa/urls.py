# Generated by Django 4.0.5 on 2022-07-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLASSIC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(default='', max_length=50, verbose_name='Автор')),
                ('briefly', models.TextField(verbose_name='Краткая информация')),
                ('book', models.FileField(upload_to='', verbose_name='Книга')),
                ('data', models.DateTimeField(verbose_name='Дата добавления')),
                ('image', models.FileField(upload_to='img/')),
            ],
            options={
                'verbose_name': 'Классика',
                'verbose_name_plural': 'Классика',
            },
        ),
    ]
