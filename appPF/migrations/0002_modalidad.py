# Generated by Django 4.1.3 on 2022-12-19 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='modalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad', models.CharField(max_length=5)),
            ],
        ),
    ]
