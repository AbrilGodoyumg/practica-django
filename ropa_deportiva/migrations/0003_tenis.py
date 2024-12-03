# Generated by Django 5.1.3 on 2024-12-01 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ropa_deportiva', '0002_accesorio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.DecimalField(choices=[('24', '24'), ('25', '25'), ('25.5', '25.5'), ('26', '26')], decimal_places=2, max_digits=10)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
