# Generated by Django 4.1.3 on 2022-12-30 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPF', '0004_busquedacompanero_delete_modalidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('cinturon', models.CharField(max_length=12)),
                ('edad', models.IntegerField()),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='nivel',
        ),
    ]
