# Generated by Django 4.1 on 2022-08-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=60)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
    ]
