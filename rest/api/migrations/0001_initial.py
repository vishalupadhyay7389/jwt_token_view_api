# Generated by Django 5.0.2 on 2024-02-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateField()),
            ],
        ),
    ]
