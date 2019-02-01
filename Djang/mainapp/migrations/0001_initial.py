# Generated by Django 2.1.5 on 2019-01-28 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('logo', models.ImageField(blank=True, upload_to='departments', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last_name')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Age')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Department')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('category', models.CharField(blank=True, max_length=30, verbose_name='К какой категории товаров относится?')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
        ),
    ]
