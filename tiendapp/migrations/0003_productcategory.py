# Generated by Django 5.1.4 on 2024-12-10 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendapp', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tiendapp.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tiendapp.product')),
            ],
        ),
    ]