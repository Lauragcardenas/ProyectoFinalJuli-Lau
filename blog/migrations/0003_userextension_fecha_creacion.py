# Generated by Django 4.0.3 on 2022-04-10 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_userextension_tarjeta_presentacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextension',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
