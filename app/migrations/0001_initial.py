# Generated by Django 3.2.5 on 2021-07-23 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Контент')),
                ('current_version', models.PositiveIntegerField(verbose_name='Поточна версія')),
            ],
            options={
                'verbose_name': 'Поточна версія',
                'verbose_name_plural': 'Поточні версії',
                'ordering': ['current_version'],
            },
        ),
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('versions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pageversion', verbose_name='Версії')),
            ],
            options={
                'verbose_name': 'Сторінка',
                'verbose_name_plural': 'Сторінки',
                'ordering': ['title'],
            },
        ),
    ]
