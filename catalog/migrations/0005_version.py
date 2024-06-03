# Generated by Django 5.0.2 on 2024-03-24 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_preview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, null=True, verbose_name=' Номер версии')),
                ('name', models.CharField(max_length=150, verbose_name='Название версии')),
                ('is_current', models.BooleanField(default=True, verbose_name='Признак актуальности')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
                'ordering': ('name',),
            },
        ),
    ]
